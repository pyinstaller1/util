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



def l01_start():
    print("로드나인 l01_start   " + time.strftime("%H:%M", time.localtime()))
    

    global wins
    wins = [win for win in gw.getWindowsWithTitle('LORDNINE') if win.title.strip()]   # LORDNINE 윈도우 목록 가져오기

    if not wins:
        print("로드나인 창이 없습니다.")
        l08_stove()

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

        ### 응답없음 체크 (l07_response => l08_stove)
        if l07_response():
            l08_stove()


        



def l02_bok():
    print("로드나인 l02_bok   " + time.strftime("%H:%M", time.localtime()))


    time.sleep(1.5)
    pyautogui.press('esc')
    time.sleep(1.5)

    scr_bok = pyautogui.screenshot(region=(left + int(width*0.527), top + int(height*0.587), int(width*0.03), int(height*0.03)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_lo_bok.png")

    """
    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results)
    if results and results[0][1].startswith(("잡", "집")):
    """


    # 녹색 픽셀 탐지
    hsv = cv2.cvtColor(scr_bok_np, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, np.array([35, 50, 50]), np.array([85, 255, 255]))

    if np.any(mask):
        print("복구 녹색 계열이 발견되었습니다.")


        # 버튼 누르기

        pyautogui.moveTo(left+(width*0.527), top+(height*0.589), 2.0) # 확인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(50)        












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







def l04_maul(on):
    print("로드나인 l04_maul   " + time.strftime("%H:%M", time.localtime()))


    if on:
        pyautogui.moveTo(left+(width*0.83), top+(height*0.70), 2.0) # 잡화상인에게 이동
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(20)     # 이동 10

        pyautogui.moveTo(left+(width*0.15), top+(height*0.23), 2.0) # 중급 HP 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        
        time.sleep(1)

        pyautogui.moveTo(left+(width*0.55), top+(height*0.6), 2.0) # 100%
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.55), top+(height*0.75), 2.0) # 구매
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()        

        pyautogui.moveTo(left+(width*0.96), top+(height*0.058), 2.0) # 종료
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        
        print("HP 회복 물약 구매 완료")


        l05_fight()
        return


        

        

    # 마을인지 OCR 체크
    scr_maul = pyautogui.screenshot(region=(left + int(width*0.8), top + int(height*0.688), int(width*0.05), int(height*0.03)))
    scr_maul_np = np.array(scr_maul)
    scr_maul.save("scr_lo_maul.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_maul_np)
    print(results)


    if results and results[0][1].startswith(("잡", "집")):
        print("여기는 마을")

        # 마을        
        pyautogui.moveTo(left+(width*0.83), top+(height*0.70), 2.0) # 잡화상인에게 이동
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(20)     # 이동 10

        pyautogui.moveTo(left+(width*0.15), top+(height*0.23), 2.0) # 중급 HP 회복
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        
        time.sleep(1)

        pyautogui.moveTo(left+(width*0.55), top+(height*0.6), 2.0) # 100%
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.55), top+(height*0.75), 2.0) # 구매
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()        

        pyautogui.moveTo(left+(width*0.96), top+(height*0.058), 2.0) # 종료
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        
        print("HP 회복 물약 구매 완료")


        l05_fight()

    else:
        print("여기는 마을 아님")




        








def l07_response():
    print("로드나인 l07_response   " + time.strftime("%H:%M", time.localtime()))


    #####
    scr_response = pyautogui.screenshot(region=(left + int(width*0.41), top + int(height*0.487), int(width*0.18), int(height*0.05)))
    scr_response_np = np.array(scr_response)
    hsv = cv2.cvtColor(scr_response_np, cv2.COLOR_RGB2HSV)

    scr_response.save("scr_lo_response.png")




    ##### 문자 인식
    # 마을인지 OCR 체크
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_response_np)
    print(results)
    print(8)



    



    if results and ("장기간" in results[0][1] or "접속" in results[0][1] or"종료" in results[0][1]):
        print("응답 녹색 계열이 발견되었습니다.")

        time.sleep(3)
        gw.getWindowsWithTitle('LORDNINE')[0].close()   # 점검이면 닫기
        time.sleep(10)

        pyautogui.moveTo(left+(width*0.57), top+(height*0.618), 2.0) # 공지 닫기
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(15)

        return True
    return False







def l08_stove():
    print("로드나인 l08_stove   " + time.strftime("%H:%M", time.localtime()))
    

    if gw.getWindowsWithTitle('STOVE'):
        # win = gw.getWindowsWithTitle('STOVE')[0]
        win = gw.getWindowsWithTitle('STOVE')[len(gw.getWindowsWithTitle('STOVE'))-1]
    else:
        print("STOVE 열기")
        ######  STOVE 여는 로직 ###########

    
    print(win.title)
    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    
    app_response = Application().connect(handle=win._hWnd)
    app_response.window(handle=win._hWnd).set_focus()

    left_response = win.left
    top_response = win.top
    width_response = win.width
    height_response = win.height

    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(0.1)



    pyautogui.moveTo(left_response+(width_response*0.62), top_response+(height_response*0.81), 2.0) # 공지 닫기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left_response+(width_response*0.88), top_response+(height_response*0.85), 2.0) # 플레이
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)   # 50




    for i in range(10):
        if gw.getWindowsWithTitle('LORDNINE'):

            win = gw.getWindowsWithTitle('LORDNINE')[0]
            print(win.title)

            global app
            app = Application().connect(handle=win._hWnd)
            app.window(handle=win._hWnd).set_focus()

            global left, top, width, height
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

            pyautogui.moveTo(left+(width*0.93), top+(height*0.08), 2.0) # Skip
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(10)




            scr_check = pyautogui.screenshot(region=(left + int(width*0.5), top + int(height*0.6), int(width*0.15), int(height*0.1)))
            scr_check_np = np.array(scr_check)
            scr_check.save("scr_lo_check.png")

            reader = easyocr.Reader(['ko', 'en'], gpu=False)
            results = reader.readtext(scr_check_np)

            print(results)

            if results and results[0][1] == "확인":
                pyautogui.moveTo(left+(width*0.6), top+(height*0.65), 2.0) # 확인
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()

                time.sleep(600)   # 600



    


            pyautogui.moveTo(left+(width*0.5), top+(height*0.7), 2.0) # 접속
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()

            time.sleep(10)
            
            pyautogui.moveTo(left+(width*0.87), top+(height*0.93), 2.0) # Start
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            
            break
        time.sleep(80)



















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

    time.sleep(60)

    pyautogui.moveTo(left+(width*0.91), top+(height*0.7), 2.0) # AUTO
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.038), top+(height*0.65), 2.0) # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()







    


def l06_heal():
    # ocr   if che < 300: b 클릭    l04_maul
    
    print("로드나인 l06_heal   " + time.strftime("%H:%M", time.localtime()))
    

    scr_che = pyautogui.screenshot(region=(left + int(width*0.287), top + int(height*0.93), int(width*0.17), int(height*0.15)))
    scr_che_np = np.array(scr_che)

    scr_che.save("scr_lo_che.png")


    # 체력 ocr 체크
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_che_np)
    print("HP ocr 점검")
    print(results)

    if results and re.sub(r"[^0-9]", "", results[0][1]):
        che = int(re.sub(r"[^0-9]", "", results[0][1]))

        if che < 1:
            print("HP가 적어서 마을로 이동")

            pyautogui.moveTo(left+(width*0.038), top+(height*0.31), 2.0) # 마을
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()

            
            time.sleep(30)
            l04_maul()
        else:
            print("HP가 마을로 충분해서 이동 안함")
    else:
        print("HP ocr 인식 오류")







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
        gw.getWindowsWithTitle('LORDNINE')[0].close()   # 로드나인 닫기
        time.sleep(5)
        


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

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")


    app_stove = Application().connect(handle=win._hWnd)

    if not (app_stove.window(handle=win._hWnd).is_enabled() and app_stove.window(handle=win._hWnd).is_visible()):
        print("창이 비활성화되어 있거나 보이지 않습니다.")
        return False

    try:
        app_stove.window(handle=win._hWnd).set_focus()
    except RuntimeError as e:
        print(f"Error: {e}")
        return False




    time.sleep(20)

    
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
        pyperclip.copy('s070092@kakao.com')
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        pyperclip.copy('s070092@nate.com')        
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        pyperclip.copy('s0700921@nate.com')
    elif os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        pyperclip.copy('ground077@naver.com')        
    else:
        pyperclip.copy('ground077@kakao.com')

    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')

    time.sleep(0.5)
    

    pyautogui.moveTo(win.left+(win.width*0.2), win.top+(win.height*0.3), 0.3) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        pyautogui.write('windows2!')
    else:
        pyautogui.write('windows1!')
        
    pyautogui.press("enter")

    time.sleep(10)



    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.28), 0.3) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.28), 3) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.28), 3) # 로드나인
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

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.1), 3) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(win.left-(win.width*0.15), win.top+(win.height*0.1), 3) # 로드나인
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(0.1)
        pyautogui.press("enter")

    l08_stove()


    time.sleep(50)







    
    # 마을인지 OCR 체크
    scr_maul = pyautogui.screenshot(region=(win.left + int(win.width*0.8), top + int(win.height*0.688), int(win.width*0.05), int(win.height*0.03)))
    scr_maul_np = np.array(scr_maul)
    scr_maul.save("scr_lo_maul.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_maul_np)
    print(results)

    time.sleep(25)


    if results and results[0][1].startswith(("잡", "집")):
        print("여기는 마을")
        l04_maul(1)   # l05_fight() 포함
    else:
        print("여기는 마을이 아닙니다.")
        pyautogui.moveTo(win.left+(win.width*0.91), top+(win.height*0.7), 2.0) # AUTO
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        time.sleep(1)


    pyautogui.moveTo(left+(win.width*0.038), top+(win.height*0.65), 2.0) # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()






def play_lo():
    try:
        l01_start()
    except Exception as e:        
        print(f"로드나인 l01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        l02_bok()
    except Exception as e:        
        print(f"로드나인 l02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        l03_jangbi()
    except Exception as e:        
        print(f"로드나인 l03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        l04_maul()   # l05_fight() 포함
    except Exception as e:        
        print(f"로드나인 l04_maul 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        l06_heal()
    except Exception as e:        
        print(f"로드나인 l06_heal 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    pyautogui.moveTo(left+(width*0.038), top+(height*0.65), 2.0) # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()




if __name__ == "__main__":
    # play_lo()
    on()
    # off()
    




