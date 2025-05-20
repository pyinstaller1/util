@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM 기존 시스템 PATH 읽기
for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path 2^>nul') do set "oldpath=%%b"

REM Python 경로가 이미 포함되어 있는지 확인
echo !oldpath! | find /I "C:\pro\Python311" >nul && (
    echo Python already in PATH. Skipping.
    goto end
)

REM Python 경로 추가
set "newpath=!oldpath!;C:\pro\Python311;C:\pro\Python311\Scripts"

REM 환경 변수 업데이트
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /d "!newpath!" /f

echo Python path safely added.
:end
pause