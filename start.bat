@echo off
chcp 65001 > nul
title 夸克視頻緩存合併工具
echo 正在啟動夸克視頻緩存合併工具...
echo.

:: 檢查Python是否安裝
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 未找到Python，請先安裝Python
    echo 您可以從以下地址下載Python：https://www.python.org/downloads/
    echo 安裝時請勾選"Add Python to PATH"選項
    echo.
    echo 按任意鍵退出...
    pause > nul
    exit /b
)

:: 檢查虛擬環境是否存在
if not exist ".venv\Scripts\activate.bat" (
    echo [信息] 虛擬環境不存在，正在創建...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo [錯誤] 無法創建虛擬環境，嘗試安裝venv模塊...
        pip install virtualenv
        python -m venv .venv
        if %errorlevel% neq 0 (
            echo [錯誤] 創建虛擬環境失敗
            echo 按任意鍵繼續不使用虛擬環境...
            pause > nul
            goto RunWithoutVenv
        )
    )
    echo [信息] 虛擬環境創建成功
)

:: 激活虛擬環境
echo [信息] 正在激活虛擬環境...
call .venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo [警告] 無法激活虛擬環境，將使用系統Python環境
    goto RunWithoutVenv
)

:: 在虛擬環境中安裝必要的模塊
echo [信息] 檢查並安裝必要的模塊...
python -c "import tkinter" > nul 2>&1
if %errorlevel% neq 0 (
    echo [信息] 安裝tkinter模塊...
    pip install tk
)

:: 在虛擬環境中運行程序
echo [信息] 在虛擬環境中運行程序...
python quark_merger.py
goto End

:RunWithoutVenv
:: 檢查必要的Python模塊
python -c "import tkinter" > nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 缺少必要的Python模塊
    echo 正在嘗試安裝...
    pip install tk
)

:: 運行程序
python quark_merger.py

:End
if %errorlevel% neq 0 (
    echo.
    echo [錯誤] 程序運行出錯
    echo 按任意鍵退出...
    pause > nul
)

:: 如果使用了虛擬環境，停用它
if defined VIRTUAL_ENV (
    deactivate
) 