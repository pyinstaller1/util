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


"""
left, top, width, height = 0, 0, 0, 0
che = 1000
app = None




import psutil

# 프로세스 이름에 'nProtect'와 관련된 부분을 찾아 종료
for proc in psutil.process_iter(attrs=['pid', 'name']):
    if 'nos' in proc.info['name']:  # 예시로 'nos'가 포함된 프로세스를 종료
        try:
            print(f"nProtect 관련 프로세스 {proc.info['name']} (PID: {proc.info['pid']}) 종료 중...")
            proc.terminate()  # 프로세스를 종료
            proc.wait()  # 종료 완료될 때까지 대기
            print(f"프로세스 {proc.info['name']} 종료 성공")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"프로세스 종료 중 오류 발생: {e}")








import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# 마우스 클릭 구조체 정의
class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long), 
                ("dy", ctypes.c_long), 
                ("mouseData", ctypes.c_ulong), 
                ("dwFlags", ctypes.c_ulong), 
                ("time", ctypes.c_ulong), 
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class Input_I(ctypes.Union):
    _fields_ = [("mi", MouseInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong), 
                ("ii", Input_I)]

# 마우스 클릭 함수
def click_mouse():
    extra = ctypes.c_ulong(0)
    
    # 마우스 버튼 눌림
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))  # MOUSEEVENTF_LEFTDOWN
    x = Input(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    # 마우스 버튼 떼기
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))  # MOUSEEVENTF_LEFTUP
    x = Input(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

# 실행
# click_mouse()
# time.sleep(1)

"""


















    




def r01_start():
    print("롬 r01_start   " + time.strftime("%H:%M", time.localtime()))


    import pydirectinput
    pydirectinput.moveTo(1100, 900, duration=1)
    pydirectinput.click()
    time.sleep(3)

    pydirectinput.moveTo(1100, 800, duration=1)
    pydirectinput.click()
    time.sleep(3)

    pydirectinput.moveTo(1100, 900, duration=1)
    pydirectinput.click()
    return



    win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[0]

    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")


    global app
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    print(777)

    

    return True







    






def r01_start1():
    print("롬 r01_start[1]   " + time.strftime("%H:%M", time.localtime()))
    
    win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[1]

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













def r02_bok():
    print("롬 r02_bok   " + time.strftime("%H:%M", time.localtime()))


    scr_start = pyautogui.screenshot(region=(left + int(width*0.38), top + int(height*0.9), int(width*0.1), int(height*0.1)))
    scr_start_np = np.array(scr_start)
    scr_start.save("scr_rom_start.png")

    # 복구 ocr 탐지
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_start_np)
    print(results)









    

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.8), 2.0)   # 복구
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.5), top+(height*0.8), 2.0)
    pyautogui.mouseUp()

    time.sleep(3)

    
    pyautogui.moveTo(left+(width*0.6), top+(height*0.75), 2.0)   # 마을
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.6), top+(height*0.75), 2.0)
    pyautogui.mouseUp()



    time.sleep(3)   # 15


    pyautogui.moveTo(left+(width*0.238), top+(height*0.087), 2.0)   # 달성도
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.238), top+(height*0.087), 2.0)   # 달성도
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    scr_bok = pyautogui.screenshot(region=(left + int(width*0.73), top + int(height*0.9), int(width*0.27), int(height*0.1)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_dal_bok.png")

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




def r03_jangbi():
    print("롬 r03_jangbi   " + time.strftime("%H:%M", time.localtime()))


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



def d04_dungeon0():
    print("달빛조각사 d04_dungeon[0]   " + time.strftime("%H:%M", time.localtime()))


    pyautogui.moveTo(left+(width*0.97), top+(height*0.07), 2.0)   # 메뉴
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.967), top+(height*0.388), 2.0)   # 월드/던전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.2), top+(height*0.5), 2.0)   # 던전0
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



def d05_dungeon1():
    print("달빛조각사 d05_dungeon[1]   " + time.strftime("%H:%M", time.localtime()))


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




def r08_kakao(mode=None):
    print("롬 r08_kakao   " + time.strftime("%H:%M", time.localtime()))

    if mode == None:
        cnt_check = 1
    elif mode == "점검":
        cnt_check = 1800

        if gw.getWindowsWithTitle('ROM : Remember Of Majesty'):
            print("점검이므로 창을 닫습니다.")

            for proc in psutil.process_iter():
                if "ROM_Launcher.exe" in proc.name():  # 프로세스 이름을 확인
                    proc.kill()  # 강제 종료



    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\Kakaogames\ROM\ROM_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ROM\ROM_Launcher.exe", shell=True)



    time.sleep(100)

    if gw.getWindowsWithTitle('ROM : Remember Of Majesty'):
        win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[0]
    else:
        time.sleep(60)
        if gw.getWindowsWithTitle('ROM : Remember Of Majesty'):
            win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[0]
        else:
            return


    print(win.title)
    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

    global app
    
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    global left, top, width, height

    left = win.left
    top = win.top
    width = win.width
    height = win.height

    pyautogui.moveTo(left+(width*0.5), top+(height*0.388), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(7)



    scr_google = pyautogui.screenshot(region=(880, 380, 380, 500))
    scr_google_np = np.array(scr_google)
    scr_google.save("scr_rom_kakao.png")

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

        if "ground077@naver" in text or "groundo77@naver" in text:
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
        subprocess.Popen(r"D:\Kakaogames\ROM\ROM_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ROM\ROM_Launcher.exe", shell=True)
        
    print("롬[0] 오픈 완료")

    time.sleep(10)
    pyautogui.moveTo(1288, 780, 1.0)   # 게임 시작
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(60)

    win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[0]


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
    















def on():
    print("롬 on   " + time.strftime("%H:%M", time.localtime()))


    import psutil

    desktop = os.environ.get('COMPUTERNAME')
    if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
        for proc in psutil.process_iter():
            if "ROM.exe" in proc.name():  # 프로세스 이름을 확인
                proc.kill()  # 강제 종료
            if "ROM_Launcher.exe" in proc.name():  # 프로세스 이름을 확인
                proc.kill()  # 강제 종료




    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\Kakaogames\ROM\ROM_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ROM\ROM_Launcher.exe", shell=True)



    time.sleep(10)


    if gw.getWindowsWithTitle('ROM : Remember Of Majesty'):
        win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[0]
    else:
        time.sleep(60)
        if gw.getWindowsWithTitle('ROM : Remember Of Majesty'):
            win = gw.getWindowsWithTitle('ROM : Remember Of Majesty')[0]
        else:
            return

    return

    print(win.left)
    print(8)

    from pynput.mouse import Controller, Button


    mouse = Controller()

    mouse.position = (win.left+(win.width*0.5), win.top+(win.height*0.388))
    mouse.click(Button.left)
    mouse.click(Button.left, 1)

    return



    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.388), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    import pydirectinput

    pydirectinput.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.388), duration=1)
    time.sleep(0.1)
    pydirectinput.click()    

    return





    from pywinauto import Application
    import psutil

    pid = None

    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == 'ROM.exe':
            print(888)
            pid = proc.info['pid']
            break

    app = Application().connect(process=pid)
    win = app.windows()[0]
    app.window(handle=win.handle).set_focus()

    print(7)


    win = win.rectangle()


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.right - win.left
    height = win.top - win.bottom

    pyautogui.moveTo(left+(width*0.5), top+(height*0.388), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    return

    time.sleep(7)



    scr_google = pyautogui.screenshot(region=(880, 380, 380, 500))
    scr_google_np = np.array(scr_google)
    scr_google.save("scr_rom_kakao.png")

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

        if "ground077@naver" in text or "groundo77@naver" in text:
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
    




















    
def play_rom(dungeon=None):
    try:
        if not r01_start():
            return
    except Exception as e:
        print(f"롬 r01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

    try:
        r02_bok()
    except Exception as e:
        print(f"롬 r02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        r03_jangbi()
    except Exception as e:
        print(f"롬 r03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")

        


    if dungeon=="던전":
        try:
            d04_dungeon0()
        except Exception as e:
            print(f"롬 r04_dungeon[0] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")



    if dungeon=="던전1":
        try:
            d05_dungeon1()
        except Exception as e:
            print(f"달빛조각사 d05_dungeon[1] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")




    """
    try:
        if not d01_start1():
            return
    except Exception as e:
        print(f"달빛조각사 d01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        d02_bok()
    except Exception as e:
        print(f"달빛조각사 d02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        d03_jangbi()
    except Exception as e:
        print(f"달빛조각사 d03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")
        


    if dungeon=="던전0":
        try:
            d04_dungeon0()
        except Exception as e:
            print(f"달빛조각사 d04_dungeon[0] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")



    if dungeon=="던전1":
        try:
            d05_dungeon1()
        except Exception as e:
            print(f"달빛조각사 d05_dungeon[1] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")
    """



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
    on()
    # r01_start()
    # play_rom()
    # check_dal()
    # play_dal("던전0")
    # play_dal("던전1")















    
