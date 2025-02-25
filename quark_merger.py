import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import codecs
import ctypes
import re
import math

class QuarkMerger:
    def __init__(self):
        # 啟用DPI感知
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass

        self.window = tk.Tk()
        self.window.title("夸克視頻緩存合併工具")
        self.window.geometry("800x600")

        # 設置默認字體
        default_font = ('Microsoft YaHei UI', 11)
        self.window.option_add('*Font', default_font)
        
        # 創建界面
        frame = ttk.Frame(self.window, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # 設置樣式
        style = ttk.Style()
        style.configure('TButton', font=default_font)
        style.configure('TCombobox', font=default_font)
        
        # 按鈕和輸入框框架
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.select_btn = ttk.Button(btn_frame, text="選擇緩存文件夾", command=self.select_folder)
        self.select_btn.pack(side=tk.LEFT, padx=5)
        
        self.output_name = ttk.Entry(btn_frame, width=30)
        self.output_name.insert(0, "output.ts")
        self.output_name.pack(side=tk.LEFT, padx=5)
        
        self.merge_btn = ttk.Button(btn_frame, text="開始合併", command=self.merge_video)
        self.merge_btn.pack(side=tk.LEFT, padx=5)
        
        # 文本輸出區
        self.text = tk.Text(frame, height=15, font=default_font)
        self.text.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 添加滾動條
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.configure(yscrollcommand=scrollbar.set)
        
        # 保存當前選擇的目錄
        self.current_folder = None
        
    def select_folder(self):
        folder = filedialog.askdirectory(title="選擇緩存文件夾")
        if not folder:
            return
            
        self.current_folder = folder
        self.text.insert(tk.END, f"已選擇文件夾：{folder}\n")
        
        # 檢查是否存在數字命名的文件
        files = []
        for f in os.listdir(folder):
            # 檢查文件是否為純數字命名
            if os.path.isfile(os.path.join(folder, f)) and f.isdigit():
                files.append(f)
        
        if not files:
            messagebox.showwarning("提示", "在選擇的文件夾中未找到數字命名的分片文件！")
            return
            
        # 對文件名按數字大小排序
        files.sort(key=lambda x: int(x))
        self.text.insert(tk.END, f"找到 {len(files)} 個分片文件\n")
        self.text.insert(tk.END, f"分片序號: {files[0]} 到 {files[-1]}\n")
        self.text.see(tk.END)
            
    def merge_batch(self, files, output_file, batch_size=100):
        total_batches = math.ceil(len(files) / batch_size)
        temp_files = []
        
        try:
            # 分批合併
            for i in range(0, len(files), batch_size):
                batch_files = files[i:i+batch_size]
                batch_num = i // batch_size + 1
                temp_output = f"temp_{batch_num}.ts"
                temp_files.append(temp_output)
                
                # 生成批處理文件
                batch_content = f'cd /d "{self.current_folder}"\n'
                quoted_files = []
                for f in batch_files:
                    quoted_files.append(f'"{f}"')
                batch_content += f'copy /b {"+".join(quoted_files)} "{temp_output}"\n'
                
                with codecs.open('merge.bat', 'w', 'gbk') as f:
                    f.write(batch_content)
                
                self.text.insert(tk.END, f"正在合併第 {batch_num}/{total_batches} 批...\n")
                self.text.see(tk.END)
                self.window.update()
                
                result = os.system('merge.bat')
                if result != 0:
                    raise Exception(f"批次 {batch_num} 合併失敗")
            
            # 合併所有臨時文件
            if len(temp_files) > 1:
                self.text.insert(tk.END, "正在合併臨時文件...\n")
                self.text.see(tk.END)
                self.window.update()
                
                batch_content = f'cd /d "{self.current_folder}"\n'
                quoted_temp_files = []
                for f in temp_files:
                    quoted_temp_files.append(f'"{f}"')
                batch_content += f'copy /b {"+".join(quoted_temp_files)} "{output_file}"\n'
                
                with codecs.open('merge.bat', 'w', 'gbk') as f:
                    f.write(batch_content)
                    
                result = os.system('merge.bat')
                if result != 0:
                    raise Exception("最終合併失敗")
            else:
                # 只有一個臨時文件，直接重命名
                os.rename(
                    os.path.join(self.current_folder, temp_files[0]),
                    os.path.join(self.current_folder, output_file)
                )
            
            # 清理臨時文件
            for temp_file in temp_files:
                try:
                    os.remove(os.path.join(self.current_folder, temp_file))
                except:
                    pass
            
            # 清理臨時的merge.bat文件
            try:
                if os.path.exists('merge.bat'):
                    os.remove('merge.bat')
            except:
                pass
                    
            return True
            
        except Exception as e:
            self.text.insert(tk.END, f"錯誤：{str(e)}\n")
            self.text.see(tk.END)
            return False
            
    def merge_video(self):
        if not self.current_folder:
            messagebox.showwarning("提示", "請先選擇文件夾！")
            return
            
        try:
            # 獲取所有數字命名的文件並排序
            files = []
            for f in os.listdir(self.current_folder):
                if os.path.isfile(os.path.join(self.current_folder, f)) and f.isdigit():
                    files.append(f)
            
            if not files:
                messagebox.showerror("錯誤", "未找到分片文件！")
                return
                
            files.sort(key=lambda x: int(x))
            
            # 生成輸出文件名
            output_file = self.output_name.get()
            if not output_file.endswith('.ts'):
                output_file += '.ts'
                
            # 開始合併
            self.text.insert(tk.END, "開始合併視頻...\n")
            self.text.see(tk.END)
            
            # 使用分批合併
            if self.merge_batch(files, output_file):
                output_path = os.path.join(self.current_folder, output_file)
                success_msg = f"合併完成！\n輸出文件：{output_path}\n"
                self.text.insert(tk.END, success_msg)
                self.text.see(tk.END)
                messagebox.showinfo("成功", "文件合併完成！")
            else:
                self.text.insert(tk.END, "合併失敗！\n")
                self.text.see(tk.END)
                messagebox.showerror("錯誤", "文件合併失敗！")
                
        except Exception as e:
            error_msg = f"錯誤：{str(e)}\n"
            self.text.insert(tk.END, error_msg)
            self.text.see(tk.END)
            messagebox.showerror("錯誤", f"發生錯誤：{str(e)}")
            
    def run(self):
        # 設置窗口最小尺寸
        self.window.minsize(600, 400)
        self.window.mainloop()

if __name__ == '__main__':
    app = QuarkMerger()
    app.run() 