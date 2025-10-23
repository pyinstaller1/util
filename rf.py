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
import pyperclip
from datetime import datetime







def github():
    print("RF github01   " + time.strftime("%H:%M", time.localtime()))

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
        url = "https://github.com/pyinstaller1/game/edit/main/rf1.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        url = "https://github.com/pyinstaller1/game/edit/main/rf2.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        url = "https://github.com/pyinstaller1/game/edit/main/rf3.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        url = "https://github.com/pyinstaller1/game/edit/main/rf4.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
        url = "https://github.com/pyinstaller1/game/edit/main/rf5.txt"

    process = subprocess.Popen([chrome_path, "--new-window", "--start-maximized", "--force-device-scale-factor=1", url])   # 크롬 열기

    time.sleep(15)

    keyboard.press_and_release('win + up')
    time.sleep(3)

    win = gw.getWindowsWithTitle('Editing game/rf')[0]
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height




    

    keyboard.press_and_release('ctrl + a')
    time.sleep(0.5)    
    keyboard.press_and_release('ctrl + x')
    time.sleep(1)

    str_temp = pyperclip.paste()

    now = datetime.now()

    global str_dungeon
    try:
        if str_dungeon:
            pass
    except:
        str_dungeon = '오류'

    
    now = now.strftime("%m%d %H:%M\t") + str_dungeon + '\n'
    str_temp = now + str_temp
    print(str_temp)
    time.sleep(1)
    pyperclip.copy(str_temp)


    keyboard.press_and_release('ctrl + v')


    time.sleep(1)
    mouse.move(left+(width*0.5), 127, absolute=True, duration=0.1)   # 스크롤 올리기
    mouse.click()
    time.sleep(0.5)
    keyboard.press_and_release('home')
    time.sleep(1)


    mouse.move(left+(width*0.95), top+(height*0.25), absolute=True, duration=0.1)   # 커밋
    mouse.click()

    time.sleep(1)

    keyboard.press_and_release('enter')

    time.sleep(8)



    for win in gw.getWindowsWithTitle('game/rf'):
        if win.title.strip():
            print(win.title.split(" - ")[0].split("·")[1].strip())
            win.close()
            break







def a01_start():
    print("RF a01_start   " + time.strftime("%H:%M", time.localtime()))

    if not gw.getWindowsWithTitle('RF ONLINE NEXT'):
        print("RF 창이 없습니다.")
        on()
        return

    win = gw.getWindowsWithTitle('RF ONLINE NEXT')[0]
    app = Application().connect(handle=win._hWnd)
    window = app.window(handle=win._hWnd)
    # window.set_focus()


    for _ in range(10):
        try:
            window.set_focus()
            break
        except RuntimeError:
            print("창이 아직 응답하지 않습니다. 1초 후 재시도...")
            time.sleep(1)
    else:
        print("창이 응답하지 않아 종료합니다.")
        exit()




    
    client_rect = window.client_rect()


    print(win.left)
    print(win.top)
    print(client_rect.left)
    print(client_rect.top)


    import win32gui
    client_left, client_top = win32gui.ClientToScreen(win._hWnd, (0, 0))

    global left, top, width, height
    left = win.left - (win.left - client_left)    
    top = win.top - (win.top - client_top)

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
        top = top * 1.05

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        top = top * 0.999


    width = client_rect.width()
    height = client_rect.height()

    
    mouse.move(int(left + width * 0.5), int(top + height * 0.5))   # 절전 해제
    time.sleep(0.1)
    mouse.press()
    time.sleep(1)    
    mouse.move(int(left + width * 0.8), int(top + height * 0.5), duration=0.3)   # 절전 해제    
    time.sleep(1)
    mouse.release()

    time.sleep(3)


    mouse.move(int(left + width * 0.5), int(top + height * 0.75))   # 확인
    mouse.click()
    time.sleep(1)
    
    mouse.move(int(left + width * 0.5), int(top + height * 0.75))   # 확인
    mouse.click()    



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



        time.sleep(1)
        time.sleep(1)
        time.sleep(1)


        mouse.move(left+(width*0.03), top+(height*0.07), absolute=True, duration=0.1)   # 지도
        mouse.click()

        time.sleep(0.5)

        mouse.move(left+(width*0.15), top+(height*0.2), absolute=True, duration=0.1)   # 지도 클릭
        mouse.click()

        time.sleep(3)


        scr = pyautogui.screenshot(region=(left + int(width*0.15), top + int(height*0.3), int(width*0.6), int(height*0.6)))
        scr.save("scr_rf_map.png")
        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(np.array(scr))
        print(results)

        for item in results:
            print(item[1][:2])
            bbox, text, confidence = item
            print(text)
            if text[:2] in ['콜드', '골드', '홀드', '콤드', '드론']:
                print(777)
                top_left = bbox[0]
                bottom_right = bbox[2]
                x = (top_left[0] + bottom_right[0]) // 2
                y = top_left[1]
                break


        mouse.move(left+(width*0.15) + x, top+(height*0.3) + y - (height*0.01), absolute=True, duration=0.1)   # 지도 클릭
        mouse.click()

        time.sleep(5)



        mouse.move(left+(width*0.53), top+(height*0.51), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()

        time.sleep(3)


        mouse.move(left+(width*0.58), top+(height*0.68), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()

        time.sleep(15)







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


    # 장비 분해
    mouse.move(left+(width*0.918), top+(height*0.05), absolute=True, duration=0.1)   # 가방
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.987), top+(height*0.25), absolute=True, duration=0.1)   # 장비
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.93), top+(height*0.97), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.55), top+(height*0.387), absolute=True, duration=0.1)   # 일반
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.65), top+(height*0.387), absolute=True, duration=0.1)   # 고급
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.55), top+(height*0.45), absolute=True, duration=0.1)   # 희귀
    mouse.click()
    time.sleep(0.5)



    mouse.move(left+(width*0.55), top+(height*0.53), absolute=True, duration=0.1)   # 장비
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.65), top+(height*0.58), absolute=True, duration=0.1)   # 수집재료
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.65), top+(height*0.71), absolute=True, duration=0.1)   # 등록가능
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.93), top+(height*0.953), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.57), top+(height*0.68), absolute=True, duration=0.1)   # 희귀 분해
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.38), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(1)




    mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    mouse.click()



    





    return




    # 일괄구매



    mouse.move(left+(width*0.973), top+(height*0.03), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(3)


    
    mouse.move(left+(width*0.88), top+(height*0.07), absolute=True, duration=0.1)   # 가방
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.07), top+(height*0.88), absolute=True, duration=0.1)   # 일괄구매
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.57), top+(height*0.78), absolute=True, duration=0.1)   # 일괄구매
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.5), top+(height*0.88), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.5), top+(height*0.88), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.963), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(3)



    # 우편
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.78), top+(height*0.96), absolute=True, duration=0.1)   # 우편
    mouse.click()
    time.sleep(1)
    
    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.21), top+(height*0.15), absolute=True, duration=0.1)   # 계정
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.963), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)


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





    time.sleep(3)




    mouse.move(int(left + width * 0.88), int(top + height * 0.07))   # 절전 해제
    mouse.click()
    time.sleep(1)


    mouse.move(int(left + width * 0.08), int(top + height * 0.88))   # 일괄 구매
    mouse.click()
    time.sleep(1)


    mouse.move(int(left + width * 0.57), int(top + height * 0.78))   # 확인
    mouse.click()
    time.sleep(0.5)
    






    time.sleep(3)

    mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    mouse.click()


    

    return




def a05_dungeon():
    print("RF a05_dungeon   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    # mouse.move(left+(width*0.73), top+(height*0.538), absolute=True, duration=0.1)   # 던전
    mouse.move(left+(width*0.73), top+(height*0.55), absolute=True, duration=0.1)   # 던전
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.38), top+(height*0.15), absolute=True, duration=0.1)   # 지역 던전
    mouse.click()
    time.sleep(3)


    mouse.move(left+(width*0.08), top+(height*0.23), absolute=True, duration=0.1)   # 안드로이드 폐기장
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 입장
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.70), top+(height*0.73), absolute=True, duration=0.1)   # 이동
    mouse.click()
    time.sleep(30)


    mouse.move(left+(width*0.15), top+(height*0.15), absolute=True, duration=0.1)   # 지도
    mouse.click()
    time.sleep(1)

    # "DESKTOP-LRGAL8H"
    # "DESKTOP-MA2NLC4"
    # "DESKTOP-792RKKB"
    # "DESKTOP-OHGK5MV"
    # "DESKTOP-H9B70U0"

    desktop = os.environ.get('COMPUTERNAME')

    if desktop == 'DESKTOP-LRGAL8H':
        
        mouse.move(left+(width*0.567), top+(height*0.267), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.587), top+(height*0.250), absolute=True, duration=0.1)   # 도보이동
        mouse.click()
        time.sleep(1)

    if desktop == 'DESKTOP-792RKKB':
        
        mouse.move(left+(width*0.567), top+(height*0.712), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.587), top+(height*0.695), absolute=True, duration=0.1)   # 도보이동
        mouse.click()
        time.sleep(1)

    if desktop == 'DESKTOP-MA2NLC4':
        
        mouse.move(left+(width*0.398), top+(height*0.51), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.418), top+(height*0.34), absolute=True, duration=0.1)   # 도보이동
        mouse.click()
        time.sleep(1)


    if desktop == 'DESKTOP-OHGK5MV':
        
        mouse.move(left+(width*0.733), top+(height*0.507), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.753), top+(height*0.488), absolute=True, duration=0.1)   # 도보이동
        mouse.click()
        time.sleep(1)


    if desktop == 'DESKTOP-H9B70U0':
        
        mouse.move(left+(width*0.773), top+(height*0.46), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.793), top+(height*0.443), absolute=True, duration=0.1)   # 도보이동
        mouse.click()
        time.sleep(1)

    time.sleep(65)


    mouse.move(left+(width*0.96), top+(height*0.61), absolute=True, duration=0.1)   # 런처
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.96), top+(height*0.61), absolute=True, duration=0.1)   # 런처
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.96), top+(height*0.61), absolute=True, duration=0.1)   # 런처
    mouse.click()
    time.sleep(1)    

    mouse.move(left+(width*0.96), top+(height*0.61), absolute=True, duration=0.1)   # 런처
    mouse.click()
    time.sleep(1)    
    
    mouse.move(left+(width*0.95), top+(height*0.78), absolute=True, duration=0.1)    # AUTO
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(3)




    # 던전 ocr 탐지
    scr = pyautogui.screenshot(region=(left + int(width*0.707), top + int(height*0.487), int(width*0.23), int(height*0.05)))
    scr.save("scr_rf_dungeon.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    global str_dungeon
    str_dungeon = "일반"
    if results:
        str_dungeon = results[0][1]
    print(str_dungeon)

    
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
            if "77@" in text or '7z@naver' in text:   # ground077@naver.com     groundo77@navercom
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




    mouse.move(left_on+(width_on*0.71), top_on+(height_on*0.65), absolute=True, duration=0.1)   # 계속
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


    
    
    time.sleep(150)


    mouse.move(left_on+(width_on*0.5), top_on+(height_on*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()


    time.sleep(15)









    win = gw.getWindowsWithTitle('RF ONLINE NEXT')[0]
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

    
    time.sleep(70)


    mouse.move(left+(width*0.95), top+(height*0.78), absolute=True, duration=0.1)   # AUTO
    mouse.click()

    time.sleep(1)


    # mouse.move(left+(width*0.03), top+(height*0.638), absolute=True, duration=0.1)   # 절전
    # mouse.click()




    # 점검 여기저기 클릭
    mouse.move(int(left + width * 0.5), int(top + height * 0.67))   # 확인
    mouse.click()
    time.sleep(1)

    mouse.move(int(left + width * 0.95), int(top + height * 0.17))   # 공지 닫기
    mouse.click()
    time.sleep(1)

    mouse.move(int(left + width * 0.5), int(top + height * 0.65))   # 확인
    mouse.click()

    
    return


























def dungeon():
    a01_start()
    a02_bok()
    a03_jangbi()    
    a05_dungeon()
    github()


    


    
def play():
    a01_start()
    a03_jangbi()





    return


    a01_start()
    a02_bok()
    a03_jangbi()










if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        elif sys.argv[1] == "off":
            off()            
        elif sys.argv[1] == "mission":
            mission()
        elif sys.argv[1] == "dungeon":
            dungeon()            
        else:
            play()
    else:
        play()
        
        # on()
        # mission()
        # off()












    
