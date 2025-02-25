# 夸克視頻緩存合併工具

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-windows-lightgrey)](https://www.microsoft.com/windows)

這是一個用於合併夸克瀏覽器緩存視頻片段的工具。它可以自動掃描並合併數字命名的視頻分片（如：0, 1, 2, 3...），生成完整的視頻文件。

## 功能特點

- 簡單易用的圖形界面
- 自動掃描視頻分片
- 支持大文件合併（數千個分片）
- 自動按數字順序排序
- 實時顯示合併進度
- 支持中文路徑
- 自動清理臨時文件
- 使用虛擬環境隔離依賴

## 系統要求

- Windows 操作系統
- Python 3.6 或更高版本
- 足夠的硬碟空間（至少是原視頻分片總大小的2倍）

## 快速開始

### 從源碼安裝

```bash
# 克隆倉庫
git clone https://github.com/linuxjackie/quark_video_merger.git
cd quark_video_merger

# 運行程序（Windows）
start.bat
```

### 直接下載
1. 從 [Releases](https://github.com/linuxjackie/quark_video_merger/releases) 頁面下載最新版本
2. 解壓縮到任意目錄
3. 運行 `start.bat`

## 安裝說明

1. 安裝 Python（如果尚未安裝）
   - 訪問 https://www.python.org/downloads/
   - 下載並安裝 Python
   - 安裝時請勾選"Add Python to PATH"選項

2. 運行程序
   - 雙擊 `start.bat`（推薦）
     - 程序會自動創建虛擬環境
     - 自動安裝所需依賴
     - 在隔離環境中運行程序
   - 或在命令行中手動運行：`python quark_merger.py`（不推薦）

## 使用方法

1. 從手機中複製夸克緩存文件夾到電腦
   - 通常在手機的 `/storage/emulated/0/Quark/Download/` 目錄下
   - 包含數字命名的分片文件（0, 1, 2, 3...）

2. 運行程序
   - 直接雙擊 `start.bat`（推薦）
   - 首次運行時會自動設置虛擬環境，可能需要等待一會兒
   - 後續運行會直接使用已創建的虛擬環境

3. 選擇文件
   - 點擊"選擇緩存文件夾"按鈕
   - 選擇包含視頻分片的文件夾
   - 程序會自動掃描並顯示找到的分片數量

4. 設置輸出
   - 在輸入框中輸入要保存的文件名
   - 默認為 output.ts
   - 如果沒有輸入 .ts 後綴，程序會自動添加

5. 開始合併
   - 點擊"開始合併"按鈕
   - 等待合併完成
   - 完成後會顯示輸出文件的位置

## 常見問題

1. 提示"未找到Python"
   - 請確保已正確安裝Python
   - 確保安裝時勾選了"Add Python to PATH"
   - 可以在命令行中運行 `python --version` 測試

2. 提示"未找到分片文件"
   - 確認選擇的文件夾是否正確
   - 確認文件夾中是否包含數字命名的文件
   - 檢查文件是否可以正常訪問

3. 合併失敗
   - 確保硬碟有足夠的空間
   - 確保對輸出目錄有寫入權限
   - 檢查是否有文件被其他程序佔用

4. 虛擬環境相關問題
   - 如果創建虛擬環境失敗，程序會自動使用系統Python環境
   - 如果需要重新創建虛擬環境，可以刪除 `.venv` 文件夾後重新運行
   - 確保系統Python版本正確且已安裝 venv 模塊

## 注意事項

- 合併過程中請勿關閉程序
- 確保有足夠的硬碟空間
- 建議在合併完成前不要打開輸出文件
- 如果出現錯誤，請查看程序窗口中的錯誤信息

## 文件說明

- `quark_merger.py`: 主程序
- `start.bat`: 啟動腳本
- `README.md`: 本說明文件

## 技術支持

如果遇到問題，請：
1. 檢查本文檔中的常見問題
2. 確認是否按照步驟正確操作
3. 查看程序窗口中的錯誤信息

## 免責聲明

本工具僅用於學習和研究目的，請勿用於非法用途。使用本工具時請遵守相關法律法規。

## 開發相關

### 目錄結構
```
quark_video_merger/
├── quark_merger.py   # 主程序
├── start.bat         # 啟動腳本
├── .gitignore       # Git忽略配置
└── README.md        # 說明文檔
```

### 環境設置
- Python 3.6+
- tkinter（GUI庫，通常包含在Python標準庫中）
- 虛擬環境（自動創建和管理）

### 貢獻指南
1. Fork 本倉庫
2. 創建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m '添加一些特性'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打開一個 Pull Request

## 版本歷史

- v1.0.0 (2024-02-25)
  - 初始版本發布
  - 基本的視頻分片合併功能
  - 添加虛擬環境支持

## 作者

LinuxJackie - [@linuxjackie](https://github.com/linuxjackie)

## 開源協議

本項目基於 MIT 協議開源 - 查看 [LICENSE](LICENSE) 文件了解更多信息

## 致謝

- 感謝所有貢獻者的付出
- 感謝 Python 和 tkinter 提供的強大支持 