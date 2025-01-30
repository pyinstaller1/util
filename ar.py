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

    # global wins
    # wins = [win for win in gw.getWindowsWithTitle('Arthdal Chronicles') if win.title.strip()]   # 아스달 윈도우 목록 가져오기



    if not gw.getWindowsWithTitle('Arthdal Chronicles'):
        print("아스달 창이 없습니다.")
        a08_netmarble()

    win = gw.getWindowsWithTitle('Arthdal Chronicles')[0]

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    global app
    app = Application().connect(handle=win._hWnd)
    






    app = Application().connect(handle=win._hWnd)

    if not (app.window(handle=win._hWnd).is_enabled() and app.window(handle=win._hWnd).is_visible()):
        print("창이 비활성화되어 있거나 보이지 않습니다.")
        return False

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

    time.sleep(2)
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.75), 3.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    return True





def a02_jangbi():
    print("a01_jangbi   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.93), top+(height*0.07), 2.0)   # 가방
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.93), top+(height*0.93), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    


    pyautogui.moveTo(left+(width*0.78), top+(height*0.93), 2.0)   # 자동선택
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




    pyautogui.moveTo(left+(width*0.78), top+(height*0.2), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.83), top+(height*0.2), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.87), top+(height*0.2), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()




    
    pyautogui.moveTo(left+(width*0.38), top+(height*0.93), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()    

    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(2)


    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 빈공간터치
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()    



    pyautogui.moveTo(left+(width*0.957), top+(height*0.07), 2.0)   # 종료
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()








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

    pyautogui.moveTo(left_response+(width_response*0.8), top_response+(height_response*0.9), 2.0) # 플레이
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)   # 60



    """
    time.sleep(3)


    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.45), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    
    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.43), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.write("ground077@naver.com")


    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.50), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.write("windows1!")


    pyautogui.moveTo(left_response+(width_response*0.5), top_response+(height_response*0.57), 2.0) # 넷마블 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left_response+(width_response*0.8), top_response+(height_response*0.9), 2.0) # 플레이
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)
    """




















    
def play_ar():
    if not a01_start():
        return
    
    a02_jangbi()


    pyautogui.moveTo(left+(width*0.038), top+(height*0.61), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


if __name__ == "__main__":
    play_ar()















    
