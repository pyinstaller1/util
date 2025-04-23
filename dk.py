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
    print("DK a01_start   " + time.strftime("%H:%M", time.localtime()))

    if not gw.getWindowsWithTitle('DK모바일 리본'):
        print("DK 창이 없습니다.")
        on_internal()
        return

    win = gw.getWindowsWithTitle('DK모바일 리본')[0]
    app = Application().connect(handle=win._hWnd)
    
    try:
        app.window(handle=win._hWnd).set_focus()
    except:    
        app.window(handle=win._hWnd).set_focus()
        
    

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    time.sleep(1)

    mouse.move(left+(width*0.6), top+(height*0.67), absolute=True, duration=0.1)   # 절전 해제
    mouse.click()
    time.sleep(1)

    return






def a02_bok():
    print("DK a02_bok   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height


    # 장시간 미입력 ocr 탐지
    scr = pyautogui.screenshot(region=(left + int(width*0.37), top + int(height*0.43), int(width*0.3), int(height*0.05)))
    scr.save("scr_dk_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)

    if results and results[0][1][:1] in ['일']:
        on()
        return 'on'


    '''
    # 대기 ocr 탐지
    scr = pyautogui.screenshot(region=(left + int(width*0.465), top + int(height*0.7), int(width*0.07), int(height*0.05)))
    scr.save("scr_dk_bok.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)
    if results and results[0][1][:2] in ['대기']:
        print(888)
    '''


    # 잡화 ocr 탐지
    scr = pyautogui.screenshot(region=(left + int(width*0.07), top + int(height*0.158), int(width*0.06), int(height*0.05)))
    scr.save("scr_dk_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    if results and results[0][1][:2] in ['잡화']:
        
        # 전투 장소로 이동
        mouse.move(left+(width*0.033), top+(height*0.31), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.18), top+(height*0.18), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(1.5)


        scr = pyautogui.screenshot(region=(left + int(width*0.38), top + int(height*0.18), int(width*0.38), int(height*0.38)))
        scr.save("scr_dk_map.png")

        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(np.array(scr))
        print(results)


        for item in results:
            bbox, text, confidence = item
            top_left = bbox[0]
            bottom_right = bbox[2]
            x = (top_left[0] + bottom_right[0]) // 2
            y = (top_left[1] + bottom_right[1]) // 2
            print(text)
            if text == '바람의 초원':
                break


        mouse.move(left + int(width*0.38) + x, top + int(height*0.18) + y, absolute=True, duration=0.1)   # 바람의 초원
        mouse.click()
        time.sleep(1)



        mouse.move(left + int(width*0.95), top + int(height*0.938), absolute=True, duration=0.1)   # 즉시 이동
        mouse.click()
        time.sleep(1)


        mouse.move(left + int(width*0.55), top + int(height*0.65), absolute=True, duration=0.1)   # 확인
        mouse.click()
        time.sleep(3)


        mouse.move(left + int(width*0.95), top + int(height*0.75), absolute=True, duration=0.1)   # AUTO
        mouse.click()
        time.sleep(1)


    











def a03_jangbi():
    print("DK a03_jangbi   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    mouse.move(left+(width*0.96), top+(height*0.08), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(0.5)


    # 드래곤나이츠
    mouse.move(left+(width*0.78), top+(height*0.25), absolute=True, duration=0.1)  # 드레곤나이츠
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.47), top+(height*0.75), absolute=True, duration=0.1)   # 레벨 상승
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()

    mouse.move(left+(width*0.6), top+(height*0.75), absolute=True, duration=0.1)   # 레벨 상승
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()      
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()  
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()

    mouse.move(left+(width*0.73), top+(height*0.75), absolute=True, duration=0.1)   # 레벨 상승
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()       
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()  
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    
    mouse.move(left+(width*0.87), top+(height*0.75), absolute=True, duration=0.1)   # 레벨 상승
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()    
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()  
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    
    time.sleep(1)
    mouse.click()


    mouse.move(left+(width*0.5), top+(height*0.93), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(0.5)


    
    # 무기숙련도
    mouse.move(left+(width*0.818), top+(height*0.25), absolute=True, duration=0.1)  # 무기숙련도
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.68), top+(height*0.85), absolute=True, duration=0.1)  # +
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)    


    mouse.move(left+(width*0.63), top+(height*0.95), absolute=True, duration=0.1)   # 저장
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.96), top+(height*0.08), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)


    # 우편
    mouse.move(left+(width*0.87), top+(height*0.93), absolute=True, duration=0.1)  # 우편
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.08), top+(height*0.2), absolute=True, duration=0.1)  # 일반
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.87), top+(height*0.87), absolute=True, duration=0.1)  # 모두 수령
    mouse.click()
    time.sleep(0.5)
    
    mouse.move(left+(width*0.17), top+(height*0.2), absolute=True, duration=0.1)  # 서버
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.87), top+(height*0.87), absolute=True, duration=0.1)  # 모두 수령
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.96), top+(height*0.15), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.96), top+(height*0.08), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(0.5)



    # 이벤트
    mouse.move(left+(width*0.73), top+(height*0.08), absolute=True, duration=0.1)   # 이벤트
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.15), top+(height*0.33), absolute=True, duration=0.1)   # 오픈기념장비패스
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.63), top+(height*0.35), absolute=True, duration=0.1)   # 미션정보
    mouse.click()
    time.sleep(0.5)



    mouse.move(left+(width*0.5), top+(height*0.7), absolute=True, duration=0.1)   # 모두수령
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()

    
    mouse.move(left+(width*0.8), top+(height*0.3), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.787), top+(height*0.818), absolute=True, duration=0.1)   # 모두수령
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()


    mouse.move(left+(width*0.15), top+(height*0.38), absolute=True, duration=0.1)   # 무한축복패스
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.63), top+(height*0.35), absolute=True, duration=0.1)   # 미션정보
    mouse.click()
    time.sleep(0.5)



    mouse.move(left+(width*0.5), top+(height*0.7), absolute=True, duration=0.1)   # 모두수령
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.8), top+(height*0.3), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.787), top+(height*0.818), absolute=True, duration=0.1)   # 모두수령
    mouse.click()
    time.sleep(0.5)
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.89), top+(height*0.128), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)




    # 출석체크
    mouse.move(left+(width*0.78), top+(height*0.08), absolute=True, duration=0.1)   # 이벤트
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.15), top+(height*0.23), absolute=True, duration=0.1)   # 오픈기념축제
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.77), top+(height*0.47), absolute=True, duration=0.1)   # 보상받기
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()

    mouse.move(left+(width*0.15), top+(height*0.27), absolute=True, duration=0.1)   # 홈페이지목표
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.77), top+(height*0.47), absolute=True, duration=0.1)   # 보상받기
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()

    mouse.move(left+(width*0.15), top+(height*0.35), absolute=True, duration=0.1)   # 오픈기념
    mouse.click()
    time.sleep(0.5)

    mouse.move(left+(width*0.77), top+(height*0.47), absolute=True, duration=0.1)   # 보상받기
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()


    mouse.move(left+(width*0.89), top+(height*0.15), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)





    # 보상
    mouse.move(left+(width*0.83), top+(height*0.08), absolute=True, duration=0.1)   # 보상
    mouse.click()
    time.sleep(0.5)



    mouse.move(left+(width*0.15), top+(height*0.23), absolute=True, duration=0.1)   # 접속시간보상
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.5), top+(height*0.77), absolute=True, duration=0.1)     # 모두받기
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()


    mouse.move(left+(width*0.15), top+(height*0.28), absolute=True, duration=0.1)   # 새턴의보상
    mouse.click()
    time.sleep(0.5)


    mouse.move(left+(width*0.78), top+(height*0.53), absolute=True, duration=0.1)     # 기본보상
    mouse.click()
    time.sleep(1)
    mouse.click()
    time.sleep(1)
    mouse.click()


    mouse.move(left+(width*0.89), top+(height*0.15), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(0.5)



    # 아이템 복구
    mouse.move(left+(width*0.68), top+(height*0.16), absolute=True, duration=0.1)   # 복구
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.25), absolute=True, duration=0.1)   # 아이템
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.3), absolute=True, duration=0.1)   # 아이템
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.73), absolute=True, duration=0.1)   # 복구
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.57), top+(height*0.63), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.88), top+(height*0.3), absolute=True, duration=0.1)   # 아이템
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.73), absolute=True, duration=0.1)   # 복구
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.57), top+(height*0.63), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.88), top+(height*0.3), absolute=True, duration=0.1)   # 아이템
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.88), top+(height*0.73), absolute=True, duration=0.1)   # 복구
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.57), top+(height*0.63), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(1)    
    


    mouse.move(left+(width*0.967), top+(height*0.187), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.83), top+(height*0.587), absolute=True, duration=0.1)   # 착용
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.83), top+(height*0.587), absolute=True, duration=0.1)   # 착용
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.83), top+(height*0.587), absolute=True, duration=0.1)   # 착용
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.033), top+(height*0.75), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(1)
    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 절전 시작
    mouse.click()
    time.sleep(1)



    return

























def a04_dungeon():
    print("DK a04_dungeon   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    mouse.move(left+(width*0.957), top+(height*0.077), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.77), top+(height*0.55), absolute=True, duration=0.1)   # 던전
    mouse.click()
    time.sleep(1.5)

    mouse.move(left+(width*0.18), top+(height*0.18), absolute=True, duration=0.1)   # 소멸던전
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.18), top+(height*0.818), absolute=True, duration=0.1)   # 비밀금고
    mouse.click()
    time.sleep(1)
    
    mouse.move(left+(width*0.693), top+(height*0.287), absolute=True, duration=0.1)   # 입장
    mouse.click()
    time.sleep(15)

    mouse.move(left + int(width*0.95), top + int(height*0.75), absolute=True, duration=0.1)   # AUTO
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.033), top+(height*0.75), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(1)
    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 절전 시작
    mouse.click()
    time.sleep(1)

    return




def a05_dungeon_week():
    print("DK a04_dungeon   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    mouse.move(left+(width*0.957), top+(height*0.077), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.77), top+(height*0.55), absolute=True, duration=0.1)   # 던전
    mouse.click()
    time.sleep(1.5)

    mouse.move(left+(width*0.18), top+(height*0.18), absolute=True, duration=0.1)   # 소멸던전
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.31), top+(height*0.817), absolute=True, duration=0.1)   # 비밀금고
    mouse.click()
    time.sleep(1)
    
    mouse.move(left+(width*0.693), top+(height*0.287), absolute=True, duration=0.1)   # 입장
    mouse.click()
    time.sleep(15)

    mouse.move(left + int(width*0.95), top + int(height*0.75), absolute=True, duration=0.1)   # AUTO
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.033), top+(height*0.75), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(1)
    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 절전 시작
    mouse.click()
    time.sleep(1)

    return











def off():
    print("DK off   " + time.strftime("%H:%M", time.localtime()))

    a01_start()



    global left, top, width, height



    mouse.move(left+(width*0.73), top+(height*0.16), absolute=True, duration=0.1)   # 오프라인 전투
    mouse.click()
    time.sleep(1)




    mouse.move(left+(width*0.53), top+(height*0.78), absolute=True, duration=0.1)   # 종료
    mouse.click()


    time.sleep(1)


    mouse.move(left+(width*0.53), top+(height*0.65), absolute=True, duration=0.1)   # 종료
    mouse.click()

    return





def on_internal():
    print("DK on   " + time.strftime("%H:%M", time.localtime()))


    for proc in psutil.process_iter():
        if "DKR.exe" in proc.name():
            proc.kill()
            print("   DK를 닫았습니다.")
        if "CrossplayLauncherAgent.exe" in proc.name():
            proc.kill()
            print("CrossplayLauncherAgent를 닫았습니다.")
        if "CrossplayRemoteLauncherAgent.exe" in proc.name():
            proc.kill()
            print("CrossplayRemoteLauncherAgent를 닫았습니다.")
        if "Hive_Launcher.exe" in proc.name():
            proc.kill()
            print("Hive_Launcher.exe를 닫았습니다.")



    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":   # 하이브 런처 열기
        subprocess.Popen([r"D:\Program Files\HiveLauncher\launcher\Hive_Launcher.exe", "hivelauncher:?app_id=com.ntrance.dkr.pc&start_point=5&envi="], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        subprocess.Popen([r"C:\Program Files\HiveLauncher\launcher\Hive_Launcher.exe", "hivelauncher:?app_id=com.ntrance.dkr.pc&start_point=5&envi="], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    time.sleep(8)

    win = gw.getWindowsWithTitle('CrossplayLauncher')[0]    
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    mouse.move(win.left+(win.width*0.88), win.top+(win.height*0.88), absolute=True, duration=0.1)   # 게임 실행
    mouse.click()
    
    time.sleep(8)


    global left, top, width, height

    win = gw.getWindowsWithTitle('DK모바일 리본')[0]


    left = win.left
    top = win.top
    width = win.width
    height = win.height


    time.sleep(30)

    mouse.move(left+(width*0.5), top+(height*0.47), absolute=True, duration=0.1)   # 구글 로그인
    mouse.click()

    time.sleep(5)    



    keyboard.press_and_release('win + up')
    time.sleep(1)    
    screen = pyautogui.size()

    scr = pyautogui.screenshot(region=(int(screen.width * 0.52), int(screen.height * 0.3), int(screen.width * 0.2), int(screen.height * 0.5)))    # 구글 계정 ocr
    scr.save("scr_dk_google.png")

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
            if "77@naver" in text:   # ground077@naver.com     groundo77@navercom
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
            
        if os.environ.get('COMPUTERNAME') in ["DESKTOP-NT06800"]:
            if "8zok" in text or "o78@k" in text:   # ground078@kakao.com       groundo8zokakaocorn   groundo78@kakao.corn
                break

    mouse.move(int(screen.width * 0.52) + x, int(screen.height * 0.3) + y, absolute=True, duration=0.1)   # 구글 로그인




    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:

        mouse.move(screen.width * 0.57, screen.height * 0.47, absolute=True, duration=0.1)   # 구글 로그인
        mouse.click()
        time.sleep(0.3)

        keyboard.write('ground077@naver.com')
        keyboard.press_and_release('enter')
        time.sleep(5)    
        keyboard.write('github001!')
        keyboard.press_and_release('enter')
        

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:

        mouse.move(screen.width * 0.57, screen.height * 0.47, absolute=True, duration=0.1)   # 구글 로그인
        mouse.click()
        time.sleep(0.3)

        keyboard.write('s070092@nate.com')
        keyboard.press_and_release('enter')
        time.sleep(5)    
        keyboard.write('github01!')
        keyboard.press_and_release('enter')
        time.sleep(5)


    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:

        mouse.move(screen.width * 0.57, screen.height * 0.47, absolute=True, duration=0.1)   # 구글 로그인
        mouse.click()
        time.sleep(0.3)

        keyboard.write('s0700921@nate.com')
        keyboard.press_and_release('enter')
        time.sleep(5)    
        keyboard.write('pyinstaller1!')
        keyboard.press_and_release('enter')
        time.sleep(5)

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:

        mouse.move(screen.width * 0.57, screen.height * 0.47, absolute=True, duration=0.1)   # 구글 로그인
        mouse.click()
        time.sleep(0.3)

        keyboard.write('ground077@kakao.com')
        keyboard.press_and_release('enter')
        time.sleep(5)    
        keyboard.write('windows1!')
        keyboard.press_and_release('enter')
        time.sleep(5)


    if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:

        mouse.move(screen.width * 0.57, screen.height * 0.47, absolute=True, duration=0.1)   # 구글 로그인
        mouse.click()
        time.sleep(0.3)

        keyboard.write('s070092@kakao.com')
        keyboard.press_and_release('enter')
        time.sleep(5)    
        keyboard.write('windows1!')
        keyboard.press_and_release('enter')
        time.sleep(5)


    if os.environ.get('COMPUTERNAME') in ["DESKTOP-NT06800"]:

        mouse.move(screen.width * 0.57, screen.height * 0.47, absolute=True, duration=0.1)   # 구글 로그인
        mouse.click()
        time.sleep(0.3)

        keyboard.write('ground078@kakao.com')
        keyboard.press_and_release('enter')
        time.sleep(5)    
        keyboard.write('windows1!')
        keyboard.press_and_release('enter')
        time.sleep(5)


    time.sleep(5)




    mouse.move(screen.width * 0.71, screen.height * 0.65, absolute=True, duration=0.1)   # 계속
    mouse.click()
    time.sleep(7)

    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(8)    

    mouse.move(left+(width*0.88), top+(height*0.918), absolute=True, duration=0.1)   # 접속
    mouse.click()
    time.sleep(25)    

    mouse.move(left+(width*0.95), top+(height*0.05), absolute=True, duration=0.1)   # 공지사항 닫기
    mouse.click()
    time.sleep(1)    




    '''
    mouse.move(left+(width*0.97), top+(height*0.2), absolute=True, duration=0.1)   # 메인퀘스트
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.55), top+(height*0.71), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(1)
    '''



    '''
    mouse.move(left+(width*0.0.033), top+(height*0.38), absolute=True, duration=0.1)   # 지도
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.2), top+(height*0.15), absolute=True, duration=0.1)   # 지도
    mouse.click()
    time.sleep(1)


    mouse.move(left+(width*0.78), top+(height*0.95), absolute=True, duration=0.1)   # 자동이동
    mouse.click()
    time.sleep(1)

    
    mouse.move(left+(width*0.97), top+(height*0.2), absolute=True, duration=0.1)   # 메인퀘스트 AUTO
    mouse.click()
    time.sleep(1)
    
    '''


    
    return






















def on():
    on_internal()
    play()






    
def dungeon():
    a01_start()
    a04_dungeon()

def dungeon_week():
    a01_start()
    a05_dungeon_week()



    
def play():
    a01_start()
    a02_bok()
    a03_jangbi()



            





if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        elif sys.argv[1] == "off":
            off()            
        elif sys.argv[1] == "dungeon":
            dungeon()
        else:
            play()
    else:
        play()
        # on()
        # mission()
        # off()












    
