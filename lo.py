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
import pyperclip
import keyboard
from pynput.mouse import Controller, Button
import sys



def l01_start():
    print("로드나인 l01_start   " + time.strftime("%H:%M", time.localtime()))


    if not gw.getWindowsWithTitle('LORDNINE'):
        on()
        return

    win = gw.getWindowsWithTitle('LORDNINE')[0]
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





        



def l02_bok():
    print("로드나인 l02_bok   " + time.strftime("%H:%M", time.localtime()))




    time.sleep(1.5)

    #####
    scr_response = pyautogui.screenshot(region=(left + int(width*0.41), top + int(height*0.487), int(width*0.18), int(height*0.05)))
    scr_response.save("scr_lo_response.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr_response))
    print(results)

    if results and ("장기간" in results[0][1] or "접속" in results[0][1] or"종료" in results[0][1]):
        print("장기간 접속 종료")
        on('on1')
        return





    time.sleep(1.5)
    pyautogui.press('esc')
    time.sleep(1.5)

    scr_bok = pyautogui.screenshot(region=(left + int(width*0.527), top + int(height*0.587), int(width*0.03), int(height*0.03)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_lo_bok.png")

    hsv = cv2.cvtColor(scr_bok_np, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, np.array([35, 50, 50]), np.array([85, 255, 255]))

    if np.any(mask):
        print("복구 녹색 계열이 발견되었습니다.")
        on()
        return




    # 마을인지 OCR 체크
    scr_maul = pyautogui.screenshot(region=(left + int(width*0.8), top + int(height*0.688), int(width*0.05), int(height*0.06)))
    scr_maul_np = np.array(scr_maul)
    scr_maul.save("scr_lo_maul.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_maul_np)
    print(results)

    if results and results[0][1].startswith(("잡", "집")):
        print("여기는 마을")
        l04_maul(1)   # l05_fight() 포함
    else:
        print("여기는 마을이 아닙니다.")
        time.sleep(5)






    












def l03_jangbi():
    print("로드나인 l03_jangbi   " + time.strftime("%H:%M", time.localtime()))




    # 장비 분해
    pyautogui.moveTo(left+(width*0.917), top+(height*0.07), 2.0) # 가방
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.957), top+(height*0.318), 2.0) # 장비
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.80), top+(height*0.53), 2.0) # 장비 47
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.687), top+(height*0.687), 2.0) # 분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    pyautogui.moveTo(left+(width*0.77), top+(height*0.83), 2.0) # 자동등록
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.38), top+(height*0.78), 2.0) # 분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.38), top+(height*0.787), 2.0) # 빈공간
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.83), top+(height*0.15), 2.0) # 분해 종료
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.95), top+(height*0.169), 2.0) # 종료
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    print("장비 분해 완료")
    


    time.sleep(3)







def l04_maul(on=None):
    print("로드나인 l04_maul   " + time.strftime("%H:%M", time.localtime()))


    # 마을        
    pyautogui.moveTo(left+(width*0.83), top+(height*0.70), 2.0) # 잡화상인에게 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(20)     # 이동 10

    pyautogui.moveTo(left+(width*0.15), top+(height*0.23), 1.0) # 중급 HP 회복
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
        
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.55), top+(height*0.6), 1.0) # 100%
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.55), top+(height*0.75), 1.0) # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()        

    pyautogui.moveTo(left+(width*0.96), top+(height*0.058), 1.0) # 종료
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
        
    print("HP 회복 물약 구매 완료")


    l05_fight()




        











def l05_fight():
    # 지도 클릭 => 3 => 울란 협곡 => ocr
    
    print("로드나인 l05_fight   " + time.strftime("%H:%M", time.localtime()))
    

    pyautogui.moveTo(left+(width*0.15), top+(height*0.23), 2.0) # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    
    
    pyautogui.moveTo(left+(width*0.028), top+(height*0.40), 2.0) # 3
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    


    pyautogui.moveTo(left+(width*0.1), top+(height*0.35), 2.0) # 울란협곡
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(2)

    # 지도의 전투 장소 ocr
    print("지도 ocr 분석")

    scr_fight = pyautogui.screenshot(region=(left + int(width*0.35), top + int(height*0.27), int(width*0.28), int(height*0.53)))
    scr_fight_np = np.array(scr_fight)
    scr_fight.save("scr_lo_fight.png")
    
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_fight_np)
    # print(results)

    list_xy = []
    
    for detection in results:
        bbox, text, confidence = detection
        top_left = bbox[0]
        bottom_right = bbox[2]

        x = (top_left[0] + bottom_right[0]) // 2
        y = (top_left[1] + bottom_right[1]) // 2
        list_xy.append([x, y])



    print(list_xy)

    rand = np.random.randint(0, 6)
    # print(np.random.randint(0, 6))
    
    # 0번 전투 장소
    pyautogui.moveTo(left + int(width*0.35) + (list_xy[0][0]), top + int(height*0.265) + (list_xy[0][1]), 2.0) # 0번 전투 장소
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.83), top+(height*0.37), 2.0) # 전투 장소
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.7), top+(height*0.71), 2.0) # 빠른 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.6), top+(height*0.57), 2.0) # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    print("전투 장소로 이동")

    time.sleep(50)

    pyautogui.moveTo(left+(width*0.91), top+(height*0.7), 2.0) # AUTO
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()









    







def off():
    print("로드나인 off   " + time.strftime("%H:%M", time.localtime()))

    win = gw.getWindowsWithTitle('LORDNINE')[0]


    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.8), top+(height*0.5), 2.0)
    pyautogui.mouseUp()

    time.sleep(3)    
        
    
    pyautogui.moveTo(left+(width*0.035), top+(height*0.317), 2.0)   # 마을
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)




    pyautogui.moveTo(left+(width*0.035), top+(height*0.638), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.5), top+(height*0.938), 2.0)   # 자동사냥
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.38), top+(height*0.8), 2.0)   # 자동사냥
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.57), top+(height*0.638), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    return


    



















def on():
    print("로드나인 on   " + time.strftime("%H:%M", time.localtime()))




        
    if gw.getWindowsWithTitle('LORDNINE'):
        os.system("taskkill /F /IM LORDNINE.exe")
        for proc in psutil.process_iter():
            if proc.name().lower() == "stove.exe":
                proc.kill()
                print(f"{proc.name()} 종료됨")

    if gw.getWindowsWithTitle('STOVE'):
        os.system("taskkill /F /IM stove.exe")
        for proc in psutil.process_iter():
            if proc.name().lower() == "stove.exe":
                proc.kill()
                print(f"{proc.name()} 종료됨")


    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\ProgramData\Smilegate\STOVE\STOVE.exe", shell=True)
    else:
        subprocess.Popen(r"C:\ProgramData\Smilegate\STOVE\STOVE.exe", shell=True)

    time.sleep(15)






    win = gw.getWindowsWithTitle('STOVE')[0]
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    time.sleep(3)


    
    # pyautogui.moveTo(win.left+(win.width*0.2), win.top+(win.height*0.23), 0.3) # 입력
    # pyautogui.mouseDown()
    
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
        keyboard.write('ground077@naver.com')
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        keyboard.write('s070092@nate.com')        
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        keyboard.write('s0700921@nate.com')
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        keyboard.write('ground077@kakao.com')
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
        keyboard.write('s070092@kakao.com')
    else:
        keyboard.write('ground077@kakao.com')

    keyboard.press_and_release('tab')
    keyboard.write('windows1!')

    keyboard.press_and_release('enter')




    global left, top, width, height




    time.sleep(10)
    win = gw.getWindowsWithTitle('STOVE')[0]

    pyautogui.moveTo(win.left+(win.width*0.07), win.top+(win.height*0.15), 1) # 로드나인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(win.left+(win.width*0.07), win.top+(win.height*0.15), 1) # 로드나인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(win.left+(win.width*0.07), win.top+(win.height*0.15), 1) # 로드나인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    

    time.sleep(1)



   


    pyautogui.moveTo(win.left+(win.width*0.83), win.top+(win.height*0.93), 1) # 플레이    
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)


    
    '''
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.28), 0.3) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.28), 1) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.28), 1) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(0.1)
        pyautogui.press("enter")

    else:
        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.1), 0.3) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.1), 1) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.1), 1) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(0.1)
        pyautogui.press("enter")
    '''




    time.sleep(30)





    win = gw.getWindowsWithTitle('LORDNINE')[0]
    print(win.title)

    # global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    pyautogui.moveTo(left+(width*0.93), top+(height*0.08), 2.0) # Skip
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)

    pyautogui.moveTo(left+(width*0.93), top+(height*0.08), 2.0) # Skip
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)

    pyautogui.moveTo(left+(width*0.93), top+(height*0.08), 2.0) # Skip
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)


    pyautogui.moveTo(left+(width*0.93), top+(height*0.08), 2.0) # Skip
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)

    pyautogui.moveTo(left+(width*0.87), top+(height*0.93), 2.0) # Start
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.6), top+(height*0.65), 2.0) # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()            


    pyautogui.moveTo(left+(width*0.5), top+(height*0.7), 2.0) # 접속
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)
            
    pyautogui.moveTo(left+(width*0.87), top+(height*0.93), 2.0) # Start
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(38)

    keyboard.press_and_release('g')

    l02_bok()



    pyautogui.moveTo(left+(width*0.038), top+(height*0.65), 2.0) # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    return


    







def play():
    try:
        l01_start()
    except Exception as e:        
        print(f"로드나인 l01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    l02_bok()
    l03_jangbi()


    '''
    try:
        l04_maul()   # l05_fight() 포함
    except Exception as e:        
        print(f"로드나인 l04_maul 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")
    '''


    global left, top, width, height

    pyautogui.moveTo(left+(width*0.038), top+(height*0.65), 2.0) # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        else:
            play()
    else:
        play()



