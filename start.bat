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

:: 檢查必要的Python模塊
python -c "import tkinter" > nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 缺少必要的Python模塊
    echo 正在嘗試安裝...
    pip install tk
)

:: 運行程序
python quark_merger.py

if %errorlevel% neq 0 (
    echo.
    echo [錯誤] 程序運行出錯
    echo 按任意鍵退出...
    pause > nul
) 