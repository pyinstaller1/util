import pyautogui
import pyperclip
import time
import os
import subprocess
import psutil
import sys
import pygetwindow as gw




# github에 올리기
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = "https://github.com/pyinstaller1/util/upload/main"
process = subprocess.Popen([chrome_path, "--new-window", "--start-maximized", url])   # 크롬 열기






pyautogui.moveTo(1000, 470, 2.0)   # choose
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp()

time.sleep(1)



pyperclip.copy(sys.argv[1])   # 파일 선택
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(1)




pyautogui.moveTo(500, 950, 2.0)   # commit
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp()


"""
:: git add total.py
:: git commit -m "Add total.py"
:: git push origin master
"""





for win in gw.getWindowsWithTitle('pyinstaller1/util - Chrome'):
    if win.title.strip():
        print(win)
        win.close()
        break




























# 각 PC에서 get.bat 실행
"""
url = "https://remotedesktop.google.com/access/session/42f654cb-bf90-3cec-f5ba-23f98a3c1f52"
url = "https://remotedesktop.google.com/access/session/9b907513-77cd-bae4-9b3f-c1797e39dfa1"
url = "https://remotedesktop.google.com/access/session/8a4b8a08-05fe-5d22-2b2e-68b96ceab806"
url = "https://remotedesktop.google.com/access/session/95af99f7-ceb3-3f84-5f0f-69068d48214c"
"""



# chrome_path = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"





url = "https://remotedesktop.google.com/access/session/42f654cb-bf90-3cec-f5ba-23f98a3c1f52"
process = subprocess.Popen([chrome_path, "--new-window", url])   # 크롬 열기

time.sleep(10)















for win in gw.getWindowsWithTitle('DESKTOP-OHGK5MV - Chrome'):
    if win.title.strip():
        print(win)
        win.close()
        break







"""


pyautogui.moveTo(300, 1017, 2.0)   # 실행창
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp()

time.sleep(1)


pyautogui.write("cmd", interval=0.1)  # 텍스트 입력
pyautogui.press('enter')
time.sleep(1)

# pyautogui.write(f"C:\\Users\\{os.getlogin()}\\get {sys.argv[1]}", interval=0.1)  # 텍스트 입력
# pyautogui.press('enter')



pyautogui.moveTo(330, 800, 2.0)   # 실행창
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp()

time.sleep(1)


pyautogui.write("cmd", interval=0.1)  # 텍스트 입력
pyautogui.press('enter')
time.sleep(1)


pyperclip.copy("cmd")   # cmd
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(0.5)
pyautogui.press('enter')
"""

