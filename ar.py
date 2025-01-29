import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui
import numpy as np
import cv2
import easyocr
import re
import psutil
import subprocess



left, top, width, height = 0, 0, 0, 0
che = 1000
wins = None
app = None










def a01_start():
    print("a01_start   " + time.strftime("%H:%M", time.localtime()))
    # print(time.strftime("%H:%M", time.localtime()))

    global wins
    wins = [win for win in gw.getWindowsWithTitle('Arthdal Chronicles') if win.title.strip()]   # 아스달 윈도우 목록 가져오기

    if not wins:
        print("윈도우를 찾을 수 없습니다.")
        a08_netmarble()
        


    elif wins:
        for i, win in enumerate(wins):
            print(f"{i + 1}: {win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")
        win = wins[0]
        print(win.title)

        global app
        app = Application().connect(handle=win._hWnd)
        app.window(handle=win._hWnd).set_focus()

        global left, top, width, height
        left = win.left
        top = win.top
        width = win.width
        height = win.height



        # 절전 화면 해제
        pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.8), top+(height*0.5), 2.0)
        pyautogui.mouseUp()


















def a02_jangbi():
    print("a01_jangbi   " + time.strftime("%H:%M", time.localtime()))

















def a08_netmarble():
    print(a08_netmarble)
    # for win in gw.getAllWindows():
    #    print(win.title)

    if gw.getWindowsWithTitle('NetmarbleLauncher'):
        win = gw.getWindowsWithTitle('NetmarbleLauncher')[0]
    else:
        print("NetmarbleLauncher 열기")
        ######  NetmarbleLauncher 여는 로직 ###########
        return


    print(win.title)
    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    
    app_response = Application().connect(handle=win._hWnd)
    app_response.window(handle=win._hWnd).set_focus()

    left_response = win.left
    top_response = win.top
    width_response = win.width
    height_response = win.height

    pyautogui.moveTo(left_response+(width_response*0.8), top_response+(height_response*0.9), 2.0) # 게임 실행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(60)

    

def play_ar():
    a01_start()
    a02_jangbi()




if __name__ == "__main__":
    play_ar()

    
