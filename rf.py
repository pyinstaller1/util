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
import sys
from pynput.mouse import Controller, Button













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

    mouse = Controller()

    mouse.position = (int(left + width * 0.5), int(top + height * 0.5))   # 절전 해제
    time.sleep(0.1)
    mouse.press(Button.left)
    time.sleep(3)
    mouse.position = (int(left + width * 0.7), int(top + height * 0.5))
    time.sleep(1)
    mouse.release(Button.left)
    time.sleep(1)


    
    mouse.position = (int(left + width * 0.5), int(top + height * 0.75))   # AUTO 종료
    mouse.click(Button.left, 1)



    

    return





def a02_bok():
    print("RF a02_bok   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height




    # 장시간 미입력 ocr 탐지
    scr = pyautogui.screenshot(region=(left + int(width*0.37), top + int(height*0.47), int(width*0.3), int(height*0.05)))
    scr.save("scr_rf_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    if results and results[0][1][:3] in ['장시간']:
        on()
        return 'on'
    

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

        time.sleep(10)

        mouse.move(left+(width*0.07), top+(height*0.07), absolute=True, duration=0.1)   # 구매
        mouse.click()
        time.sleep(0.5)


        mouse.move(left+(width*0.1), top+(height*0.238), absolute=True, duration=0.1)   # 치료제    0.238
        mouse.click()
        time.sleep(0.5)


        mouse.move(left+(width*0.558), top+(height*0.538), absolute=True, duration=0.1)   # MAX
        mouse.click()
        time.sleep(0.5)


        mouse.move(left+(width*0.5), top+(height*0.77), absolute=True, duration=0.1)   # 구매
        mouse.click()
        time.sleep(0.5)
  

        mouse.move(left+(width*0.03), top+(height*0.083), absolute=True, duration=0.2)   # 닫기
        mouse.click()



        '''
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
        '''


        time.sleep(1)
        time.sleep(1)
        time.sleep(1)


        mouse.move(left+(width*0.03), top+(height*0.07), absolute=True, duration=0.1)   # 지도
        mouse.click()

        time.sleep(0.5)

        mouse.move(left+(width*0.15), top+(height*0.2), absolute=True, duration=0.1)   # 지도 클릭
        mouse.click()

        time.sleep(1)


        scr = pyautogui.screenshot(region=(left + int(width*0.2), top + int(height*0.3), int(width*0.5), int(height*0.5)))
        scr.save("scr_rf_map.png")
        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(np.array(scr))
        print(results)

        for item in results:
            print(item[1][:2])
            bbox, text, confidence = item
            print(text)
            if text[:2] in ['콜드', '골드', '홀드', '콤드']:
                print(777)
                top_left = bbox[0]
                bottom_right = bbox[2]
                x = (top_left[0] + bottom_right[0]) // 2
                y = top_left[1]
                break


        mouse.move(left+(width*0.3) + x, top+(height*0.3) + y - (height*0.01), absolute=True, duration=0.1)   # 지도 클릭
        mouse.click()

        time.sleep(3)



        mouse.move(left+(width*0.53), top+(height*0.51), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()

        time.sleep(1)


        mouse.move(left+(width*0.58), top+(height*0.68), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()

        time.sleep(15)


        # 콜드
        keyboard.press('up')
        keyboard.press('right')
        time.sleep(5)
        keyboard.release('up')
        keyboard.release('right')
        # 콜드





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

    '''
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    '''

    mouse.move(left+(width*0.917), top+(height*0.07), absolute=True, duration=0.1)   # 가방
    mouse.click()

    mouse.move(left+(width*0.97), top+(height*0.27), absolute=True, duration=0.1)   # 장비
    mouse.click()

    mouse.move(left+(width*0.93), top+(height*0.95), absolute=True, duration=0.1)   # 분해
    mouse.click()

    mouse.move(left+(width*0.55), top+(height*0.3988), absolute=True, duration=0.1)   # 일반
    mouse.click()

    mouse.move(left+(width*0.65), top+(height*0.3988), absolute=True, duration=0.1)   # 고급
    mouse.click()

    mouse.move(left+(width*0.55), top+(height*0.53), absolute=True, duration=0.1)   # 장비
    mouse.click()

    mouse.move(left+(width*0.93), top+(height*0.95), absolute=True, duration=0.1)   # 분해
    mouse.click()

    time.sleep(0.1)

    mouse.move(left+(width*0.38), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    
    time.sleep(0.5)


    mouse.move(left+(width*0.977), top+(height*0.123), absolute=True, duration=0.1)   # 장비
    mouse.click()

    mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    mouse.click()

    return




def a04_mission():
    print("RF a04_mission   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height


    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()

    time.sleep(0.5)

    mouse.move(left+(width*0.83), top+(height*0.468), absolute=True, duration=0.1)   # 미션
    mouse.click()

    time.sleep(0.5)


    for i in range(10):
        mouse.move(left+(width*0.87), top+(height*0.917), absolute=True, duration=0.1)   # 수락
        mouse.click()
        time.sleep(0.1)
 

    mouse.move(left+(width*0.5), top+(height*0.3), absolute=True, duration=0.1)   # 미션
    mouse.click()
    time.sleep(0.1)


    mouse.move(left+(width*0.87), top+(height*0.917), absolute=True, duration=0.1)   # 진행
    mouse.click()
    time.sleep(0.1)


    mouse.move(left+(width*0.58), top+(height*0.68), absolute=True, duration=0.1)   # 즉시 이동
    mouse.click()



    
        
    # mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 닫기
    # mouse.click()



    mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    mouse.click()


    

    return




















def off():
    print("RF off   " + time.strftime("%H:%M", time.localtime()))

    a01_start()



    global left, top, width, height


    mouse.move(left+(width*0.977), top+(height*0.03), absolute=True, duration=0.1)   # 종료
    mouse.click()

    time.sleep(1)


    mouse.move(left+(width*0.65), top+(height*0.65), absolute=True, duration=0.1)   # 오프라인 모드
    mouse.click()

    time.sleep(1)

    mouse.move(left+(width*0.57), top+(height*0.85), absolute=True, duration=0.1)   # 오프라인 모드
    mouse.click()








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
        
    time.sleep(15)
    

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
    time.sleep(5)



    


    mouse.move(left_on+(width_on*0.5), top_on+(height_on*0.46), absolute=True, duration=0.1)   # 구글 로그인
    mouse.click()
    time.sleep(10)


    keyboard.press_and_release('win + up')
    time.sleep(2)    

    scr = pyautogui.screenshot(region=(left_on + int(width_on*0.5), top_on + int(height_on*0.3), int(width_on*0.3), int(height_on*0.6)))   # 구글 계정 ocr
    scr.save("scr_rf_google.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    for item in results:
        bbox, text, confidence = item
        top_left = bbox[0]
        bottom_right = bbox[2]
        x = (top_left[0] + bottom_right[0]) // 2
        y = (top_left[1] + bottom_right[1]) // 2


        if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
            if "77@" in text:   # ground077@naver.com     groundo77@navercom
                break
            
        if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
            if "92@n" in text:   # s070092@nate.com
                break

        if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
            if "921@n" in text:   # s0700921@nate.com
                break            


        if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
            if "7zok" in text or "o77@k" in text:   # ground077@kakao.com       groundo7zokakaocorn   groundo77@kakao.corn
                break


        if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
            if "92@k" in text:   # s070092@kakao.com
                break

        '''
        if os.environ.get('COMPUTERNAME') in ["DESKTOP-NT06800"]:
            if "92@k" in text:   # s070092@kakao.com
                break
        '''


            
    print('   OCR 구글계정: ' + text)


    mouse.move(left_on+(width_on*0.5) + x, top_on+(height_on*0.3) + y, absolute=True, duration=0.1)   # 계정 클릭
    mouse.click()

    time.sleep(2)


    mouse.move(left_on+(width_on*0.71), top_on+(height_on*0.67), absolute=True, duration=0.1)   # 계속
    mouse.click()

    time.sleep(3)


    app.window(handle=win._hWnd).set_focus()
    time.sleep(5)   


    mouse.move(left_on+(width_on*0.1), top_on+(height_on*0.87), absolute=True, duration=0.1)   # 게임 실행
    mouse.click()


    # time.sleep(3)
    # mouse.move(left_on+(width_on*0.5), top_on+(height_on*0.43), absolute=True, duration=0.1)   # 확인
    # mouse.click()
    
    time.sleep(8)



    mouse.move(left_on+(width_on*0.38), top_on+(height_on*0.46), absolute=True, duration=0.1)   # AMD 그래픽 드라이버
    mouse.click()
    time.sleep(1)
    keyboard.press_and_release('esc')
    time.sleep(3)


    
    
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

    
    time.sleep(80)


    mouse.move(left+(width*0.95), top+(height*0.78), absolute=True, duration=0.1)   # AUTO
    mouse.click()

    a02_bok()


    mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    mouse.click()
    
    return





























    
def mission():
    a01_start()
    a04_mission()





    
def play():
    a01_start()
    if a02_bok() != 'on':
        pass
        # a03_jangbi()









if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        elif sys.argv[1] == "mission":
            mission()
        else:
            play()
    else:
        play()
        # on()
        # mission()
        # off()












    
