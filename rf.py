import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui
import numpy as np
import easyocr
import re
import psutil
import subprocess
import os
import keyboard, mouse













def a01_start():
    print("RF a01_start   " + time.strftime("%H:%M", time.localtime()))

    if not gw.getWindowsWithTitle('RF 온라인 넥스트'):
        print("RF 창이 없습니다.")
        on()
        return

    win = gw.getWindowsWithTitle('RF 온라인 넥스트')[0]
    app = Application().connect(handle=win._hWnd)
    
    try:
        print(7)
        app.window(handle=win._hWnd).set_focus()
    except:
        print(8)
        time.sleep(1)        
        app.window(handle=win._hWnd).set_focus()
        
    

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 절전 해제
    mouse.press()
    mouse.move(left+(width*0.7), top+(height*0.5), absolute=True, duration=0.3)
    mouse.release()
    time.sleep(2)



    return





def a02_bok():
    print("RF a02_bok   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    # 복구 ocr 탐지
    scr = pyautogui.screenshot(region=(left + int(width*0.077), top + int(height*0.07), int(width*0.05), int(height*0.05)))
    scr.save("scr_rf_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    if results and results[0][1] in ['잡화 상인']:

        x = left + int(width*0.077) + (results[0][0][0][0] + results[0][0][1][0])//2
        y = top + int(height*0.07) + (results[0][0][0][1] + results[0][0][2][1])//2

        mouse.move(x, y, absolute=True, duration=0.1)   # 잡화 상인
        mouse.click()

        time.sleep(3)

        mouse.move(left+(width*0.07), top+(height*0.07), absolute=True, duration=0.1)   # 구매
        mouse.click()


        mouse.move(left+(width*0.1), top+(height*0.238), absolute=True, duration=0.1)   # 치료제    0.238
        mouse.click()

        mouse.move(left+(width*0.558), top+(height*0.538), absolute=True, duration=0.1)   # MAX
        mouse.click()

        mouse.move(left+(width*0.5), top+(height*0.77), absolute=True, duration=0.1)   # 구매
        mouse.click()

        mouse.move(left+(width*0.03), top+(height*0.083), absolute=True, duration=0.2)   # 구매
        mouse.click()

        mouse.move(left+(width*0.738), top+(height*0.083), absolute=True, duration=0.5)   # 복구
        mouse.click()

        mouse.move(left+(width*0.5), top+(height*0.818), absolute=True, duration=0.1)   # 복구
        mouse.click()
        time.sleep(0.5)
        mouse.click()
        time.sleep(0.5)
        mouse.click()
        time.sleep(0.5)
        mouse.click()
        time.sleep(0.5)
        mouse.click()        




        mouse.move(left+(width*0.03), top+(height*0.07), absolute=True, duration=0.1)   # 지도
        mouse.click()

        time.sleep(0.1)

        mouse.move(left+(width*0.15), top+(height*0.2), absolute=True, duration=0.1)   # 지도 클릭
        mouse.click()

        time.sleep(1)


        scr = pyautogui.screenshot(region=(left + int(width*0.3), top + int(height*0.3), int(width*0.5), int(height*0.5)))
        scr.save("scr_rf_map.png")
        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(np.array(scr))
        print(results)

        for item in results:
            bbox, text, confidence = item
            if text in ['스카디 골짜기']:
                top_left = bbox[0]
                bottom_right = bbox[2]
                x = (top_left[0] + bottom_right[0]) // 2
                y = top_left[1]
                break


        mouse.move(left+(width*0.3) + x, top+(height*0.3) + y - (height*0.01), absolute=True, duration=0.1)   # 지도 클릭
        mouse.click()

        mouse.move(left+(width*0.53), top+(height*0.51), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()

        mouse.move(left+(width*0.58), top+(height*0.68), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()

        time.sleep(8)

        mouse.move(left+(width*0.95), top+(height*0.78), absolute=True, duration=0.1)   # AUTO
        mouse.click()

        time.sleep(1)


        # mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
        # mouse.click()

        # mouse.move(left+(width*0.5), top+(height*0.67), absolute=True, duration=0.1)   # 확인
        # mouse.click()
        
    return













def a03_jangbi():
    print("RF a03_jangbi   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()




    return























def off():
    print("RF off   " + time.strftime("%H:%M", time.localtime()))



    win = gw.getWindowsWithTitle('RF 온라인 넥스트')[0]
    app = Application().connect(handle=win._hWnd)
    
    try:
        app.window(handle=win._hWnd).set_focus()
    except:
        time.sleep(1)        
        app.window(handle=win._hWnd).set_focus()
        
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 절전 해제
    mouse.press()
    mouse.move(left+(width*0.7), top+(height*0.5), absolute=True, duration=0.3)
    mouse.release()
    time.sleep(2)

    
        



    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.8), top+(height*0.5), 2.0)
    pyautogui.mouseUp()

    time.sleep(2)








def on():
    print("RF on   " + time.strftime("%H:%M", time.localtime()))


    for proc in psutil.process_iter():
        if "projectrf.exe" in proc.name().lower():
            proc.kill()
        if "ProjectRF-Win64-Shipping.exe" in proc.name():
            proc.kill()
            print("   RF를 닫았습니다.")
        if "Netmarble Launcher.exe" in proc.name():
            proc.kill()            



    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":   # 넷마블 열기
        subprocess.Popen([r"D:\Program Files\Netmarble\Netmarble Launcher\Netmarble Launcher.exe"] + ["--productcode=/Game/rfnext", "--build"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    else:
        subprocess.Popen([r"C:\Program Files\Netmarble\Netmarble Launcher\Netmarble Launcher.exe"] + ["--productcode=/Game/rfnext", "--build"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    time.sleep(10)
    

    for i in range(10):
        if gw.getWindowsWithTitle('NetmarbleLauncher'):
            win = gw.getWindowsWithTitle('NetmarbleLauncher')[0]
            break
        time.sleep(10)

    
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    left_on = win.left
    top_on = win.top
    width_on = win.width
    height_on = win.height

    mouse.move(left_on+(width_on*0.1), top_on+(height_on*0.87), absolute=True, duration=0.1)   # 게임 실행
    mouse.click()
    time.sleep(3)




    mouse.move(left_on+(width_on*0.38), top_on+(height_on*0.46), absolute=True, duration=0.1)   # AMD 그래픽 드라이버
    mouse.click()
    time.sleep(1)
    keyboard.press_and_release('esc')
    time.sleep(3)
    


    mouse.move(left_on+(width_on*0.5), top_on+(height_on*0.46), absolute=True, duration=0.1)   # 구글 로그인
    mouse.click()
    time.sleep(8)    

    scr = pyautogui.screenshot(region=(left_on + int(width_on*0.5), top_on + int(height_on*0.3), int(width_on*0.3), int(height_on*0.6)))   # 구글 계정 ocr
    scr.save("scr_rf_google.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    # print(results)


    for item in results:
        bbox, text, confidence = item
        top_left = bbox[0]
        bottom_right = bbox[2]
        x = (top_left[0] + bottom_right[0]) // 2
        y = (top_left[1] + bottom_right[1]) // 2


        if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
            if "77@" in text:   # ground077@naver.com     groundo77@navercom
                break
            
        if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
            if "7zok" in text:   # ground077@kakao.com       groundo7zokakaocorn
                break
            
        if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
            if "92@n" in text:   # s070092@nate.com
                break

        if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
            if "921@n" in text:   # s0700921@nate.com
                break            

        if os.environ.get('COMPUTERNAME') in ["DESKTOP-NT06800"]:
            if "92@k" in text:   # s070092@kakao.com
                break    


            
    print('   OCR 구글계정: ' + text)


    mouse.move(left_on+(width_on*0.5) + x, top_on+(height_on*0.3) + y, absolute=True, duration=0.1)   # 계정 클릭
    mouse.click()

    time.sleep(2)


    mouse.move(left_on+(width_on*0.63) + x, top_on+(height_on*0.55) + y, absolute=True, duration=0.1)   # 계속
    mouse.click()


    app.window(handle=win._hWnd).set_focus()
    time.sleep(5)   


    mouse.move(left_on+(width_on*0.1), top_on+(height_on*0.87), absolute=True, duration=0.1)   # 게임 실행
    mouse.click()

    
    time.sleep(88)


    mouse.move(left_on+(width_on*0.5), top_on+(height_on*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()


    time.sleep(10)









    win = gw.getWindowsWithTitle('RF 온라인 넥스트')[0]
    app = Application().connect(handle=win._hWnd)
    
    try:
        app.window(handle=win._hWnd).set_focus()
    except:
        time.sleep(1)        
        app.window(handle=win._hWnd).set_focus()
        
    

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height





    mouse.move(left+(width*0.88), top+(height*0.938), absolute=True, duration=0.1)   # 선택하기
    mouse.click()

    
    time.sleep(30)



    
    return





























    
def dungeon_ar():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아스달 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        a04_se()
    except Exception as e:
        print(f"아스달 a04_se 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    pyautogui.moveTo(left+(width*0.038), top+(height*0.61), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()





    
def play():
    a01_start()
    # a02_bok()
    a03_jangbi()







if __name__ == "__main__":
    play()
    # on()



















    
