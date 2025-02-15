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



# left, top, width, height = 0, 0, 0, 0
che = 1000
app = None










def a01_start():
    print(7)



    print("아레스 a01_start   " + time.strftime("%H:%M", time.localtime()))



    if not gw.getWindowsWithTitle('아레스'):
        print("아레스 창이 없습니다.")
        a08_kakao()
        return True

    """
    if len(gw.getWindowsWithTitle('아레스')) == 1:
        print("창이 1개만 있으므로 닫습니다.")

        for proc in psutil.process_iter():
            if "Ares.exe" in proc.name():  # 프로세스 이름을 확인
                proc.kill()  # 강제 종료
        d08_XL()
        return True
    """

        

    win = gw.getWindowsWithTitle('아레스')[0]

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    global app
    app = Application().connect(handle=win._hWnd)

    if not (app.window(handle=win._hWnd).is_enabled() and app.window(handle=win._hWnd).is_visible()):
        print("창이 비활성화되어 있거나 보이지 않습니다.")
        return False

    try:
        app.window(handle=win._hWnd).set_focus()
    except RuntimeError as e:
        print(f"Error: {e}")
        return False


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height



    pyautogui.moveTo(left+(width*0.5), top+(height*0.65), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.65), 2.0)
    pyautogui.mouseUp()



    return True





def a01_start1():
    print("아레스 a01_start[1]   " + time.strftime("%H:%M", time.localtime()))
    
    win = gw.getWindowsWithTitle('아레스')[1]

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    global app
    app = Application().connect(handle=win._hWnd)

    if not (app.window(handle=win._hWnd).is_enabled() and app.window(handle=win._hWnd).is_visible()):
        print("창이 비활성화되어 있거나 보이지 않습니다.")
        return False

    try:
        app.window(handle=win._hWnd).set_focus()
    except RuntimeError as e:
        print(f"Error: {e}")
        return False


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    return True













def a02_bok():
    print("아레스 a02_bok   " + time.strftime("%H:%M", time.localtime()))


    time.sleep(3)



    scr_bok = pyautogui.screenshot(region=(left + int(width*0.005), top + int(height*0.1), int(width*0.03), int(height*0.05)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ares_bok.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)

    if results[0][1][0] != "광":
        return


    

    pyautogui.moveTo(left+(width*0.178), top+(height*0.12), 2.0)   # 복구
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)


    pyautogui.moveTo(left+(width*0.55), top+(height*0.73), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    



    
    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(3)



    """
    scr_map = pyautogui.screenshot(region=(left + int(width*0.417), top + int(height*0.38), int(width*0.15), int(height*0.15)))
    scr_map_np = np.array(scr_map)
    scr_map.save("scr_ares_map.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_map_np)
    print(results)
    """


    pyautogui.moveTo(left+(width*0.423), top+(height*0.415), 1.0)   # 잡화상인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()









    time.sleep(5)

    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.51), 2.0)   # 잡화상인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(12)


    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.56), top+(height*0.56), 2.0)   # MAX
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.71), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.97), top+(height*0.05), 2.0)   # X
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(1)


    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)    

    pyautogui.moveTo(left+(width*0.03), top+(height*0.95), 2.0)   # 행성지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.7), top+(height*0.21), 2.0)   # 갈라테하빙하
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.53), top+(height*0.57), 2.0)   # 안식처
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)   

    pyautogui.moveTo(left+(width*0.65), top+(height*0.77), 2.0)   # 자동이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(50)

    pyautogui.press('g')
    

    return






    



    scr_bok = pyautogui.screenshot(region=(left + int(width*0.73), top + int(height*0.9), int(width*0.27), int(height*0.1)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ares_bok.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results)

    if results and results[0][1].startswith("잡"):
        pyautogui.moveTo(left+(width*0.28), top+(height*0.087), 2.0)   # 복구
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.5), top+(height*0.83), 2.0)   # 경험치 회복
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.5), top+(height*0.83), 2.0)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.738), top+(height*0.18), 2.0)   # X
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.738), top+(height*0.18), 2.0)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.77), top+(height*0.908), 2.0)   # 잡화 상인
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.77), top+(height*0.908), 2.0)
        pyautogui.mouseUp()


        time.sleep(5)



        pyautogui.moveTo(left+(width*0.15), top+(height*0.5), 2.0)   # 농축 HP 물약
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.15), top+(height*0.5), 2.0)
        pyautogui.mouseUp()                 


        pyautogui.moveTo(left+(width*0.67), top+(height*0.75), 2.0)   # 100%
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.67), top+(height*0.75), 2.0)
        pyautogui.mouseUp()
        
        pyautogui.moveTo(left+(width*0.6), top+(height*0.87), 2.0)   # 구매
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.6), top+(height*0.87), 2.0)
        pyautogui.mouseUp()
        

        pyautogui.moveTo(left+(width*0.33), top+(height*0.08), 2.0)   # X
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.33), top+(height*0.08), 2.0)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.15), top+(height*0.3), 2.0)   # 지도
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.15), top+(height*0.3), 2.0)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.35), top+(height*0.38), 2.0)   # 스텔라포트
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.35), top+(height*0.38), 2.0)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.97), top+(height*0.08), 2.0)   # X
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.97), top+(height*0.08), 2.0)
        pyautogui.mouseUp()
        


        pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 스텔라포트
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.57), top+(height*0.617), 2.0)   # 확인
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.moveTo(left+(width*0.57), top+(height*0.617), 2.0)
        pyautogui.mouseUp()        

    
    return




def d03_jangbi():
    print("달빛조각사 d03_jangbi   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.918), top+(height*0.078), 2.0)   # 가방
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.8), top+(height*0.818), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.37), top+(height*0.918), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.37), top+(height*0.918), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.37), top+(height*0.918), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.37), top+(height*0.918), 2.0)   # 분해
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # X
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




    print("장비 분해 완료")

    return



def a04_dungeon():
    print("아레스 던전   " + time.strftime("%H:%M", time.localtime()))



    """
    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 메뉴
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.1), top+(height*0.58), 3.0)   # 경쟁
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.38), top+(height*0.38), 2.0)   # 모리아기지
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(20)

    pyautogui.moveTo(left+(width*0.07), top+(height*0.15), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)

    
    pyautogui.moveTo(left+(width*0.25), top+(height*0.2587), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(5)
    """





    pyautogui.moveTo(left+(width*0.87), top+(height*0.07), 2.0)   # SHOP
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)


    pyautogui.moveTo(left+(width*0.05), top+(height*0.95), 2.0)   # 골드일괄구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()







    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)


    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)    

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.77), 2.0)   # 구매
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    



    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # X
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.3), top+(height*0.5), 2.0)   # 자동이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()










    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



def a05_dungeon_week():
    print("아레스 주간던전   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 메뉴
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.967), top+(height*0.388), 2.0)   # 월드/던전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 던전1
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.15), top+(height*0.53), 2.0)   # 6층
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.9), top+(height*0.918), 2.0)   # 던전입장
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(5)


    pyautogui.moveTo(left+(width*0.03), top+(height*0.398), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




















def a08_kakao(mode=None):
    print("아레스 a08_kakao   " + time.strftime("%H:%M", time.localtime()))

    if mode == None:
        cnt_check = 1
    elif mode == "점검":
        cnt_check = 1800

        if gw.getWindowsWithTitle('아레스'):
            print("점검이므로 창을 닫습니다.")

            for proc in psutil.process_iter():
                if "Ares.exe" in proc.name():  # 프로세스 이름을 확인
                    proc.kill()  # 강제 종료
                if "ARES_Launcher.exe" in proc.name():  # 프로세스 이름을 확인
                    proc.kill()  # 강제 종료

        

    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)

    time.sleep(50)





    win = gw.getWindowsWithTitle('ARES Launcher')[0]

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")


    app_kakao = Application().connect(handle=win._hWnd)

    if not (app_kakao.window(handle=win._hWnd).is_enabled() and app_kakao.window(handle=win._hWnd).is_visible()):
        print("창이 비활성화되어 있거나 보이지 않습니다.")
        return False

    try:
        app_kakao.window(handle=win._hWnd).set_focus()
    except RuntimeError as e:
        print(f"Error: {e}")
        return False

    time.sleep(5)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.5), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(1)


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.17), 2.0) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H", "DESKTOP-792RKKB"]:
        pyautogui.write('ground077')
    else:
        pyautogui.write('ground077@naver.com')
    pyautogui.press("enter")
    

    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.3), 0.3) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.write('windows1!')
    pyautogui.press("enter")





    time.sleep(10)






    win = gw.getWindowsWithTitle('ARES Launcher')[1]

    pyautogui.moveTo(win.left+(win.width*0.87), win.top+(win.height*0.78), 2.0) # 게임 실행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(50)






    win = gw.getWindowsWithTitle('아레스')[0]



    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time,sleep(3)
    return










    ###################


    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(30)


    pyautogui.moveTo(left+(width*0.88), top+(height*0.77), 2.0)   # 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)

    pyautogui.moveTo(left+(width*0.83), top+(height*0.25), 2.0)   # X
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.press("g")

    ###################
    
    

    if gw.getWindowsWithTitle('아레스'):
        win = gw.getWindowsWithTitle('아레스')[0]
    else:
        return


    print(win.title)
    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    global app
    
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    # global left, top, width, height

    left = win.left
    top = win.top
    width = win.width
    height = win.height

    pyautogui.moveTo(left+(width*0.5), top+(height*0.388), 2.0) # 구글로 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(7)



    scr_google = pyautogui.screenshot(region=(880, 380, 380, 500))
    scr_google_np = np.array(scr_google)
    scr_google.save("scr_dal_google.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_google_np)
    print(results)



    str_start = ""
    x_start = 0
    y_start = 0

    for detection in results:
        bbox, text, confidence = detection
        top_left = bbox[0]
        bottom_right = bbox[2]
        x = (top_left[0] + bottom_right[0]) // 2
        y = (top_left[1] + bottom_right[1]) // 2


        # groundo77@navercom   s070092@nate corr

        if "ground077@naver.com" in text or "groundo77@navercom" in text:
            str_start = text
            x_start = x
            y_start = y
            break


    print(text)
    print(x_start * 10000 + y_start)


    # ID 클릭
    pyautogui.moveTo(880 + x_start, 380 + y_start, 2.0)   # ID 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    app.window(handle=win._hWnd).set_focus()


    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 클릭
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(15)



    # 점검
    pyautogui.moveTo(left+(width*0.65), top+(height*0.7), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    print(f"점검 시작 {time.strftime('%H:%M', time.localtime())}")

    ##########
    time.sleep(cnt_check)   # 점검 30분
    ##########
    
    print(f"점검 완료 {time.strftime('%H:%M', time.localtime())}")

    pyautogui.moveTo(left+(width*0.87), top+(height*0.93), 2.0)   # 캐릭터 선택
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    time.sleep(30)




    pyautogui.moveTo(left+(width*0.918), top+(height*0.128), 2.0)   # 광고 제거
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(3)


    pyautogui.moveTo(left+(width*0.957), top+(height*0.75), 2.0)   # AUTO 
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    
    pyautogui.moveTo(left+(width*0.03), top+(height*0.398), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    ####################
    ### [0]
    ####################


    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)
        
    print("아레스 오픈 완료")

    time.sleep(10)
    pyautogui.moveTo(1288, 780, 1.0)   # 게임 시작
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(60)

    win = gw.getWindowsWithTitle('아레스')[0]


    print(win.title)
    print(f"{win.title} (위치[0]: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    # global app
    
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    # global left, top, width, height

    left = win.left
    top = win.top
    width = win.width
    height = win.height



    pyautogui.moveTo(left+(width*0.5), top+(height*0.388), 2.0) # 구글로 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(8)



    scr_google = pyautogui.screenshot(region=(880, 380, 380, 500))
    scr_google_np = np.array(scr_google)
    scr_google.save("scr_dal_google[0].png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_google_np)
    print(results)



    str_start = ""
    x_start = 0
    y_start = 0

    for detection in results:
        bbox, text, confidence = detection
        top_left = bbox[0]
        bottom_right = bbox[2]
        x = (top_left[0] + bottom_right[0]) // 2
        y = (top_left[1] + bottom_right[1]) // 2


        # groundo77@navercom   s070092@nate corr

        if "s070092@nate.com" in text or "070092@nate" in text:
            str_start = text
            x_start = x
            y_start = y
            break


    print(text)
    print(x_start * 10000 + y_start)


    # ID 클릭
    pyautogui.moveTo(880 + x_start, 380 + y_start, 2.0)   # ID 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    app.window(handle=win._hWnd).set_focus()


    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 클릭
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(15)


    # 점검
    pyautogui.moveTo(left+(width*0.65), top+(height*0.7), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.87), top+(height*0.93), 2.0)   # 캐릭터 선택
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    time.sleep(30)


    pyautogui.moveTo(left+(width*0.918), top+(height*0.128), 2.0)   # 광고 제거
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(3)


    pyautogui.moveTo(left+(width*0.957), top+(height*0.75), 2.0)   # AUTO 
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    














def dungeon_ares():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a04_dungeon()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a04_dungeon()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")











    
def play_ares(dungeon=None):
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a02_bok()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")





    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start[1] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        a02_bok()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")









    pyautogui.moveTo(left+(width*0.03), top+(height*0.398), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




def check_dal():
    try:
        d08_XL("점검")
    except Exception as e:
        print(f"달빛조각사 d01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        d02_bok()
    except Exception as e:
        print(f"달빛조각사 d03_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        d03_jangbi()
    except Exception as e:
        print(f"달빛조각사 d02_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")   









if __name__ == "__main__":
    play_ares()
    # check_dal()

    # dungeon_ares()















    
