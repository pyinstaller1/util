import time
from datetime import datetime
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
import pyperclip
import sys
from pynput.mouse import Controller, Button











def github():
    print("뱀피르 github01   " + time.strftime("%H:%M", time.localtime()))

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
        url = "https://github.com/pyinstaller1/game/edit/main/vp1.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        url = "https://github.com/pyinstaller1/game/edit/main/vp2.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        url = "https://github.com/pyinstaller1/game/edit/main/vp3.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        url = "https://github.com/pyinstaller1/game/edit/main/vp4.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
        url = "https://github.com/pyinstaller1/game/edit/main/vp5.txt"

    process = subprocess.Popen([chrome_path, "--new-window", "--start-maximized", "--force-device-scale-factor=1", url])   # 크롬 열기

    time.sleep(20)




    win = gw.getWindowsWithTitle('Editing game/vp')[0]
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    keyboard.press_and_release('win + up')
    time.sleep(3)

    keyboard.press_and_release('ctrl + a')
    time.sleep(0.5)    
    keyboard.press_and_release('ctrl + x')
    time.sleep(1)

    str_temp = pyperclip.paste()

    now = datetime.now()

    global str_support, str_purchase
    # str_support = "초원"
    # str_purchase = "구매"


    try:
        if str_support:
            pass
    except:
        str_support = '오류'


    try:
        if str_purchase:
            pass
    except:
        str_purchase = '오류'

        
    
    now = now.strftime("%m%d %H:%M\t") + str_support + "\t" + str_purchase + '\n'
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



    for win in gw.getWindowsWithTitle('game/vp'):
        if win.title.strip():
            print(win.title.split(" - ")[0].split("·")[1].strip())
            win.close()
            break






def a01_start(check='0'):
    print("뱀피르 a01_start   " + time.strftime("%H:%M", time.localtime()))


    if not gw.getWindowsWithTitle('VAMPIR'):
        print("뱀피르 창이 없습니다.")
        on()
        return



    win = gw.getWindowsWithTitle('VAMPIR')[0]
    app = Application().connect(handle=win._hWnd)

    time.sleep(1)        

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


    mouse.move(int(left + width * 0.5), int(top + height * 0.5))   # 절전 해제
    time.sleep(0.1)
    mouse.press()
    time.sleep(1)    
    mouse.move(int(left + width * 0.8), int(top + height * 0.5), duration=0.3)   # 절전 해제    
    time.sleep(1)
    mouse.release()
    time.sleep(3)
    
    return







def a02_bok():
    print("VP a02_bok   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    scr = pyautogui.screenshot(region=(left + int(width*0.38), top + int(height*0.45), int(width*0.05), int(height*0.05)))
    scr.save("scr_vp_jang.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)
    
    if results and results[0][1][:1] in ['장', '잠']:
        keyboard.press_and_release('space')
        time.sleep(10)

        mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
        mouse.click()
        time.sleep(15)

        mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 게임 시작
        mouse.click()
        time.sleep(25)
        

    
    scr = pyautogui.screenshot(region=(left + int(width*0.45), top + int(height*0.917), int(width*0.1), int(height*0.05)))
    scr.save("scr_vp_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    if results and results[0][1] in ['거점 부활']:
        keyboard.press_and_release('space')
        time.sleep(25)


        mouse.move(left+(width*0.81), top+(height*0.73), absolute=True, duration=0.1)   # 잡화상
        mouse.click()
        time.sleep(10)

        mouse.move(left+(width*0.1), top+(height*0.23), absolute=True, duration=0.1)   # 소형 HP 물약
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.5), top+(height*0.63), absolute=True, duration=0.1)   # 75%
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.55), top+(height*0.77), absolute=True, duration=0.1)   # 구매
        mouse.click()
        time.sleep(1)

        keyboard.press_and_release('esc')
        time.sleep(1)

        return








def a021_support():
    print("뱀피르 a021_support   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height



    # 장비 분해
    mouse.move(left+(width*0.917), top+(height*0.07), absolute=True, duration=0.1)   # 가방
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.78), top+(height*0.83), absolute=True, duration=0.1)   # 일괄분해
    mouse.click()
    time.sleep(2)


    mouse.move(left+(width*0.9), top+(height*0.83), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.9), top+(height*0.83), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)



    mouse.move(left+(width*0.87), top+(height*0.07), absolute=True, duration=0.1)   # 상점
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.07), top+(height*0.93), absolute=True, duration=0.1)   # 일괄구매
    mouse.click()
    time.sleep(3)

    keyboard.press_and_release('space')
    time.sleep(3.5)

    global str_purchase

    scr = pyautogui.screenshot(region=(left + int(width*0.46), top + int(height*0.3), int(width*0.1), int(height*0.1)))
    scr.save("scr_vp_pucharse.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    if results:
        print(results[0][1])
        str_purchase = results[0][1].replace(' ', '')
    else:
        str_purchase = "No"
    


    keyboard.press_and_release('space')
    time.sleep(3.5)

    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(3)
    

    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(2)



    mouse.move(left+(width*0.97), top+(height*0.57), absolute=True, duration=0.1)   # Support
    mouse.click()
    time.sleep(5)



    mouse.move(left+(width*0.1), top+(height*0.93), absolute=True, duration=0.1)   # 실행
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.1), top+(height*0.93), absolute=True, duration=0.1)   # 실행
    mouse.click()
    time.sleep(18)

    

    mouse.move(left+(width*0.023), top+(height*0.78), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(5)


    global str_support

    scr = pyautogui.screenshot(region=(left + int(width*0.033), top + int(height*0.12), int(width*0.1), int(height*0.07)))
    scr.save("scr_vp_support.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    if results:
        print(results[0][1])
        str_support = results[0][1].replace(' ', '')
    else:
        str_support = "No"

    github()
        

    
    return










def a03_jangbi():
    print("뱀피르 a03_jangbi   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    '''
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    '''




    # 업적
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(2)


    mouse.move(left+(width*0.96), top+(height*0.387), absolute=True, duration=0.1)   # 업적
    mouse.click()
    time.sleep(8)

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    



    # 우편
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(2)


    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(2)


    mouse.move(left+(width*0.76), top+(height*0.95), absolute=True, duration=0.1)   # 우편
    mouse.click()
    time.sleep(5)


    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.2), top+(height*0.15), absolute=True, duration=0.1)   # 계정
    mouse.click()
    time.sleep(1)    


    mouse.move(left+(width*0.6), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.6), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)
    
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)







    # 장비 분해
    mouse.move(left+(width*0.917), top+(height*0.07), absolute=True, duration=0.1)   # 가방
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.78), top+(height*0.83), absolute=True, duration=0.1)   # 일괄분해
    mouse.click()
    time.sleep(2)


    mouse.move(left+(width*0.9), top+(height*0.83), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.9), top+(height*0.83), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.917), top+(height*0.07), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)





def a031_stop():
    print("뱀피르 a031_stop   " + time.strftime("%H:%M", time.localtime()))


    if not gw.getWindowsWithTitle('VAMPIR'):
        print("뱀피르 창이 없습니다.")
        on()
        return


    win = gw.getWindowsWithTitle('VAMPIR')[0]
    app = Application().connect(handle=win._hWnd)

    time.sleep(1)        

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
    
    mouse.move(left+(width*0.023), top+(height*0.78), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(5)







def a04_change(play_time=1):
    print("뱀피르 a04_change   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height


    # 캐릭터 변경
    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.97), top+(height*0.93), absolute=True, duration=0.1)   # 캐릭터 변경
    mouse.click()
    time.sleep(15)

    if play_time == 1:
        mouse.move(left+(width*0.88), top+(height*0.35), absolute=True, duration=0.1)   # 1번 플레이어        
        mouse.click()
        time.sleep(3)

    if play_time == 2:
        mouse.move(left+(width*0.88), top+(height*0.46), absolute=True, duration=0.1)   # 2번 플레이어
        mouse.click()
        time.sleep(3)

    if play_time == 3:
        mouse.move(left+(width*0.88), top+(height*0.58), absolute=True, duration=0.1)   # 3번 플레이어
        mouse.click()    
        time.sleep(3)



    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 게임 시작
    mouse.click()


    time.sleep(30)

    # a021_support()

    return





    # time.sleep(25)









    return






































def off():
    print("뱀피르 off   " + time.strftime("%H:%M", time.localtime()))

    a01_start()

    global left, top, width, height

    mouse.move(left+(width*0.97), top+(height*0.07), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.917), top+(height*0.93), absolute=True, duration=0.1)   # 비접속 모드
    mouse.click()
    time.sleep(1)


    keyboard.press_and_release('space') 
    time.sleep(1)

    
    return

    








def on():
    print("뱀피르 on   " + time.strftime("%H:%M", time.localtime()))


    for proc in psutil.process_iter():
        if "ProjectRED-Win64-Shipping.exe" in proc.name():
            proc.kill()
            print("   뱀피르를 닫았습니다.")
        if "Netmarble Launcher.exe" in proc.name():
            proc.kill()
            print("   뱀피르를 닫았습니다.")


    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":   # 넷마블 열기
        subprocess.Popen([r"D:\Program Files\Netmarble\Netmarble Launcher\Netmarble Launcher.exe"] + ["--productcode=/Game/thered", "--buildcode=A"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    else:
        subprocess.Popen([r"C:\Program Files\Netmarble\Netmarble Launcher\Netmarble Launcher.exe"] + ["--productcode=/Game/thered", "--buildcode=A"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    time.sleep(15)
    

    for i in range(10):
        if gw.getWindowsWithTitle('NetmarbleLauncher'):
            print('     NetmarbleLauncher')
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

    
    time.sleep(15)


    mouse.move(left_on+(width_on*0.38), top_on+(height_on*0.46), absolute=True, duration=0.1)   # AMD 그래픽 드라이버
    mouse.click()
    time.sleep(1)
    keyboard.press_and_release('esc')

    time.sleep(30)






    win = gw.getWindowsWithTitle('VAMPIR')[0]
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


    mouse.move(left_on+(width_on*0.5), top_on+(height_on*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()

    time.sleep(10)



    '''
    mouse.move(left+(width*0.88), top+(height*0.35), absolute=True, duration=0.1)   # 1번 플레이어
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.88), top+(height*0.46), absolute=True, duration=0.1)   # 2번 플레이어
    mouse.click()
    time.sleep(3)
    '''


    mouse.move(left+(width*0.88), top+(height*0.58), absolute=True, duration=0.1)   # 3번 플레이어
    mouse.click()    
    time.sleep(3)

    

    mouse.move(left+(width*0.88), top+(height*0.95), absolute=True, duration=0.1)   # 게임 시작
    mouse.click()

    time.sleep(25)



    mouse.move(left+(width*0.97), top+(height*0.06), absolute=True, duration=0.1)   # 메뉴
    mouse.click()

    time.sleep(300)



    return




















def play():
    a01_start()
    a02_bok()    
    a03_jangbi()
    a031_stop()
    
def dungeon(play_time = 1):
    a01_start()
    a02_bok()
    a04_change(play_time)
    a03_jangbi()
    a021_support()

    return
    








if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        elif sys.argv[1] == "off":
            off()
        elif sys.argv[1] == "dungeon":
            dungeon(int(sys.argv[2]))

            
        elif sys.argv[1] == "github":
            a01_start()
            a021_support()
            github()
        else:
            play()
    else:
        play()
        # on()
        # mission()
        # off()












    
