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
import os
import webbrowser
import pyperclip



left, top, width, height = 0, 0, 0, 0
che = 1000
wins = None
app = None










def s01_start():
    print("아키에이지 s01_start   " + time.strftime("%H:%M", time.localtime()))


    if not gw.getWindowsWithTitle('ArcheAge WAR'):
        on()
        return




    win = gw.getWindowsWithTitle('ArcheAge WAR')[0]

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    time.sleep(0.1)




    pyautogui.moveTo(left+(width*0.5), top+(height*0.33), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.33), 2.0)
    pyautogui.mouseUp()

    time.sleep(1)


    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    return











def s02_maul():
    print("아키에이지 s02_maul   " + time.strftime("%H:%M", time.localtime()))

    time.sleep(1)

    # 마을 ocr 탐지
    scr_maul = pyautogui.screenshot(region=(int(width * 0.3), int(height * 0.12), int(width * 0.1), int(height * 0.1)))
    scr_maul_np = np.array(scr_maul)
    scr_maul.save("scr_ak_maul.png")
    
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_maul_np)
    print(results)

    if results and results[0][1][1] == "의":
        print("여기는 마을")

    
        pyautogui.moveTo(left+(width*0.687), top+(height*0.07), 2.0)   # 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.15), top+(height*0.3), 2.0)   # 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.15), top+(height*0.43), 0.5)   # 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
    

        pyautogui.moveTo(left+(width*0.15), top+(height*0.5), 0.5)   # 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
    
        pyautogui.moveTo(left+(width*0.15), top+(height*0.57), 0.5)   # 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.15), top+(height*0.7), 0.5)   # 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.6), top+(height*0.63), 0.5)   # 확인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(1)








def s03_map():
    print("아키에이지 s03_map   " + time.strftime("%H:%M", time.localtime()))

    time.sleep(1)



    pyautogui.moveTo(left+(width*0.1), top+(height*0.15), 0.5)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)



    # 맵 ocr 탐지
    scr_maul = pyautogui.screenshot(region=(int(width * 0.12), int(height * 0.38), int(width * 0.18), int(height * 0.6)))
    scr_maul_np = np.array(scr_maul)
    scr_maul.save("scr_ak_map.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_maul_np)

    x, y = 0, 0

    list_map = ['쇠의 길', '쇠바람 고개', '여름잎 강가', '강철 실험장']
    
    for item in results:
        int_map = int(time.strftime('%S', time.localtime())) % len(list_map)
        if int_map == 3: int_map = 1
        if item[1] == list_map[int_map]:
            x = (item[0][0][0] + item[0][1][0]) // 2
            y = (item[0][1][1] + item[0][2][1]) // 2
            break
        


    pyautogui.moveTo(int(width * 0.12)+x, int(height * 0.38)+y, 2.0)   # 쇠의 길
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(int(width * 0.9), int(height * 0.97), 2.0)   # 순간 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()            

    pyautogui.moveTo(int(width * 0.65), int(height * 0.68), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(10)

    pyautogui.press('f')

    time.sleep(1)    

    return
        









def s04_jangbi():
    print("아키에이지 s04_jangbi   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.81), top+(height*0.07), 1.0)   # 가방
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.838), top+(height*0.15), 1.0)   # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    
    pyautogui.moveTo(left+(width*0.95), top+(height*0.71), 0.5)   # 장비 선택
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.93), top+(height*0.8), 0.5)   # 돋보기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.797), top+(height*0.8), 0.5)   # 쓰레기통
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(int(width * 0.65), int(height * 0.68), 0.5)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)



    pyautogui.moveTo(left+(width*0.95), top+(height*0.71), 0.5)   # 장비 선택
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.93), top+(height*0.8), 0.5)   # 돋보기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.797), top+(height*0.8), 0.5)   # 쓰레기통
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(int(width * 0.65), int(height * 0.68), 0.5)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)



    pyautogui.moveTo(left+(width*0.95), top+(height*0.71), 0.5)   # 장비 선택
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.93), top+(height*0.8), 0.5)   # 돋보기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.797), top+(height*0.8), 0.5)   # 쓰레기통
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(int(width * 0.65), int(height * 0.68), 0.5)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(0.5)

    pyautogui.press('esc')
    time.sleep(0.5)

    pyautogui.press('esc')
    time.sleep(0.5)



    pyautogui.moveTo(left+(width*0.81), top+(height*0.07), 1.0)   # 가방
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.81), top+(height*0.8), 0.5)   # 분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.787), top+(height*0.7), 0.5)   # 일반
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.838), top+(height*0.7), 0.5)   # 고급
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.81), top+(height*0.8), 0.5)   # 분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(int(width * 0.65), int(height * 0.68), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(0.5)

    pyautogui.press('esc')
    time.sleep(0.5)

    pyautogui.press('esc')
    time.sleep(0.5)

    return







































def on():
    print("아키에이지 on   " + time.strftime("%H:%M", time.localtime()))


    if gw.getWindowsWithTitle('ArcheAge WAR'):
        os.system("taskkill /F /IM ArcheAgeWAR.exe")
        os.system("taskkill /F /IM Q7-Win64-Shipping.exe")

    webbrowser.open("https://aw.game.daum.net/aw/")

    time.sleep(1)
    pyautogui.hotkey('win', 'up')
    time.sleep(1)

    x, y = pyautogui.size()

    
    desktop = os.environ.get('COMPUTERNAME')

    if desktop in ["DESKTOP-LRGAL8H"]:
        pyautogui.moveTo(x*0.8, y*0.15, 0.5)   # login
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(x*0.8, y*0.15, 2.0)   # login
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(x*0.8, y*0.15, 2.0)   # login
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()        
    
        pyperclip.copy("ground077@naver.com")

        
    if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
        pyautogui.moveTo(x*0.8, y*0.12, 0.5)   # login
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(x*0.8, y*0.12, 2,0)   # login
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(x*0.8, y*0.12, 2.0)   # login
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()        
        
        pyperclip.copy("ground077")

    pyautogui.moveTo(x*0.553, y*0.308, 0.5)   # login
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()        
        

    pyautogui.moveTo(x*0.5, y*0.308, 0.5)   # login
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)

    for i in range(30):
        pyautogui.press('backspace')  # 백스페이스 키 누름
        

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)


    for i in range(6):
        pyautogui.press('tab')
        time.sleep(0.5)

    pyautogui.press('enter')



    time.sleep(3)

    pyautogui.moveTo(x*0.95, y*0.2, 0.5)   # Game Start
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    time.sleep(80)




    win = gw.getWindowsWithTitle('ArcheAge WAR')[0]

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    time.sleep(0.1)



    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(10)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)

    pyautogui.moveTo(int(width * 0.9), int(height * 0.97), 2.0)   # 게임하기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()            

    pyautogui.moveTo(int(width * 0.65), int(height * 0.68), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(15)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.moveTo(int(width * 0.5), int(height * 0.25), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    

    play()
    
    return













































    
def play():
    try:
        s01_start()
    except Exception as e:
        print(f"아키에이지 s01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        s02_maul()
    except Exception as e:
        print(f"아키에이지 s02_maul 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        s03_map()
    except Exception as e:
        print(f"아키에이지 s03_map 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        s04_jangbi()
    except Exception as e:
        print(f"아키에이지 s04_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")



    pyautogui.moveTo(left+(width*0.048), top+(height*0.93), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.5), top+(height*0.33), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.33), 2.0)
    pyautogui.mouseUp()


if __name__ == "__main__":
    # play()
    on()




















    
