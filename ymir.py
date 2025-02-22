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








def s01_start():
    print("이미르 s01_start   " + time.strftime("%H:%M", time.localtime()))

    win = gw.getWindowsWithTitle('Ymir  ')[0]

    global app
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height
 
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 절전 화면 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.5), 2.0)
    pyautogui.mouseUp()











        



def s02_bok():
    print("이미르 s02_bok   " + time.strftime("%H:%M", time.localtime()))


    time.sleep(3)
    
    # 복구 ocr 탐지
    scr_bok = pyautogui.screenshot(region=(left + int(width*0.0388), top + int(height*0.08), int(width*0.07), int(height*0.05)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ymir_bok.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results)

    if results[0][1][0] == "의":
        print("여기는 마을")
    else:
        return

        


    pyautogui.moveTo(left+(width*0.05), top+(height*0.15), 2.0)   # 잡화상인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(15)


    pyautogui.moveTo(left+(width*0.15), top+(height*0.15), 0.3)   # 물약
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.178), top+(height*0.23), 0.3)   # +100
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.178), top+(height*0.23), 0.1)   # +100
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.55), top+(height*0.93), 0.3)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.973), top+(height*0.07), 0.3)   # X
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(2)


    pyautogui.press('m')   # 지도
    time.sleep(1)


    pyautogui.moveTo(left+(width*0.25), top+(height*0.11), 0.3)   # 우탄가르드
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.87), top+(height*0.37), 0.3)   # 우탄가르드
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.97), top+(height*0.95), 0.3)   # 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    time.sleep(100)

    pyautogui.press('x')









    # 던전
    """
    pyautogui.moveTo(left+(width*0.91), top+(height*0.07), 0.3)   # SHOP
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(2)

    pyautogui.moveTo(left+(width*0.2), top+(height*0.07), 0.3)   # SHOP
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(2)
    """







    return















def s03_jangbi():
    print("이미르 s03_jangbi   " + time.strftime("%H:%M", time.localtime()))

    # 컬렉션 장비분해 일일미션 우편




    # 컬렉션

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.61), top+(height*0.51), 0.5) # 컬렉션
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.5), top+(height*0.25), 0.5) # 컬렉션
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.87), top+(height*0.93), 0.5) # 일괄등록
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.58), top+(height*0.61), 0.5) # 등록
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)



    # 장비 분해


    pyautogui.press("i")
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.90), top+(height*0.95), 0.3)   # 일괄분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.587), top+(height*0.43), 0.3)   # 일반
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.73), top+(height*0.53), 0.3)   # 분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)
    
    pyautogui.moveTo(left+(width*0.73), top+(height*0.53), 0.3)   # 분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)
    
    pyautogui.press("i")
    time.sleep(1)







    # 일일미션

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.47), top+(height*0.388), 0.5) # 일일미션
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.888), top+(height*0.17), 0.5) # 모두받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.888), top+(height*0.17), 0.5) # 모두받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    

    # 우편

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.7), top+(height*0.58), 0.5) # 우편
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.93), top+(height*0.12), 0.5) # 모두받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.93), top+(height*0.12), 0.5) # 모두받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)



    
    return





def s04_dungeon():
    print("이미르 s04_dungeon   " + time.strftime("%H:%M", time.localtime()))

    # 임무 업적 상점


    # 임무

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.41), top+(height*0.388), 0.5) # 임무
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.07), top+(height*0.2), 0.5) # 우탄가르드
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)
    

    pyautogui.moveTo(left+(width*0.888), top+(height*0.888), 0.5) # 수락
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.8), top+(height*0.95), 0.5) # 자동진행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.78), top+(height*0.78), 0.5) # 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    time.sleep(15)



    # 업적

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.53), top+(height*0.58), 0.5) # 업적
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.93), top+(height*0.12), 0.5) # 모두받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.93), top+(height*0.12), 0.5) # 모두받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.96), top+(height*0.05), 0.5) # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    # 상점
    pyautogui.press('f9')
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.1), top+(height*0.12), 0.5) # 교환
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.3), top+(height*0.33), 0.3) # 발키리카드1
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.55), top+(height*0.77), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.55), top+(height*0.77), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.5), top+(height*0.33), 0.3) # 다사르카드1
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.55), top+(height*0.77), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.55), top+(height*0.77), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)





    # 소모품
    pyautogui.moveTo(left+(width*0.038), top+(height*0.28), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    pyautogui.moveTo(left+(width*0.5), top+(height*0.28), 1.0) # 방어구강화석
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)



    pyautogui.moveTo(left+(width*0.65), top+(height*0.7), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)

    pyautogui.moveTo(left+(width*0.55), top+(height*0.77), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.5)


    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)


    return






def on():
    print("이미르 on   " + time.strftime("%H:%M", time.localtime()))


    """
    if gw.getWindowsWithTitle('Ymir  '):
        gw.getWindowsWithTitle('Ymir  ')[0].close()   # 이미르 닫기
        time.sleep(5)

    time.sleep(10)   # 100
    """

    win = gw.getWindowsWithTitle('Ymir  ')[0]
    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 1.0) # Start
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    time.sleep(50)

    pyautogui.moveTo(left+(width*0.938), top+(height*0.938), 0.5) # 캐릭터선택
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(50)


    # 복구 ocr 탐지
    scr_bok = pyautogui.screenshot(region=(left + int(width*0.0388), top + int(height*0.08), int(width*0.07), int(height*0.05)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ymir_bok.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results)

    if results[0][1][0] == "의":
        s02_bok()
    else:
        pyautogui.press('x')

    pyautogui.moveTo(left+(width*0.038), top+(height*0.65), 2.0) # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



def play():
    try:
        s01_start()
    except Exception as e:
        try:
            s01_start()
        except Exception as e:
            try:
                s01_start()
            except Exception as e:
                try:
                    s01_start()
                except Exception as e:
                    try:
                        s01_start()
                    except Exception as e:
                        print(f"이미르 01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")
    try:
        s02_bok()
    except Exception as e:        
        print(f"이미르 s02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")



    try:
        s03_jangbi()
    except Exception as e:        
        print(f"이미르 s03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    
    """
    try:
        s04_dungeon()
    except Exception as e:        
        print(f"이미르 s04_dungeon 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")
    """


    pyautogui.moveTo(left+(width*0.28), top+(height*0.88), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()










if __name__ == "__main__":
    # play()
    on()
    




