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
    url = "https://github.com/pyinstaller1/game/edit/main/odin.txt"


    process = subprocess.Popen([chrome_path, "--new-window", "--start-maximized", "--force-device-scale-factor=1", url])   # 크롬 열기

    time.sleep(15)

    keyboard.press_and_release('win + up')
    time.sleep(3)



    win = gw.getWindowsWithTitle('Editing game/odin')[0]
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

    keyboard.press_and_release('ctrl + a')
    time.sleep(0.5)    
    keyboard.press_and_release('ctrl + x')
    time.sleep(1)

    str_temp = pyperclip.paste()

    now = datetime.now()

    global github_character, github_dungeon, github_results
    # github_character = 1
    # github_dungeon = 2
    # github_results = '균열의 입구'


    try:
        if github_character:
            pass
    except:
        github_character = '오류'


    try:
        if github_dungeon:
            pass
    except:
        github_dungeon = '오류'

    try:
        if github_results:
            pass
    except:
        github_results = '오류'


    
    now = now.strftime("%m%d %H:%M\t") + str(github_character) + "번캐릭\t" + str(github_dungeon) + "번던전\t" + github_results + '\n'
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



    for win in gw.getWindowsWithTitle('game/odin'):
        if win.title.strip():
            print(win.title.split(" - ")[0].split("·")[1].strip())
            win.close()
            break






def a01_start():
    print("오딘 a01_start   " + time.strftime("%H:%M", time.localtime()))

    if not gw.getWindowsWithTitle('ODIN'):
        print("오딘 창이 없습니다.")
        on()
        return


    for t in gw.getAllTitles():
        if "ODIN" in t:   # 제목에 'ODIN' 포함된 경우
            win = gw.getWindowsWithTitle(t)[0]
            time.sleep(1)
            app = Application().connect(handle=win._hWnd)
            try:
                app.window(handle=win._hWnd).set_focus()
            except:
                time.sleep(1)        
                app.window(handle=win._hWnd).set_focus()
            break


    time.sleep(1)

    try:
        app.window(handle=win._hWnd).set_focus()
    except:
        time.sleep(1)        
        app.window(handle=win._hWnd).set_focus()

    time.sleep(1)

    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    mouse.move(int(left + width * 0.6), int(top + height * 0.5))   # 절전 해제
    time.sleep(0.1)
    mouse.press()
    time.sleep(1)    
    mouse.move(int(left + width * 0.77), int(top + height * 0.5), duration=0.1)   # 절전 해제    
    time.sleep(1)
    mouse.release()
    time.sleep(3)
    
    return







def a02_bok():
    print("오딘 a02_bok   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height
    flag_bok = False


    # mouse.move(left+(width*0.5), top+(height*0.63), absolute=True, duration=0.1)   # 장시간 확인
    # mouse.click()
    # time.sleep(1)
        


    scr = pyautogui.screenshot(region=(left + int(width*0.38), top + int(height*0.47), int(width*0.15), int(height*0.07)))
    scr.save("scr_odin_jang.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)

    if results and results[0][1][:1] in ['장', '잠']:   # 장시간
        print(results[0][1])
        mouse.move(int(left + (width * 0.5)), int(top + (height * 0.63)), absolute=True, duration=0.1)   # 확인
        mouse.click()
        time.sleep(15)
        # on()


        # 오딘 창
        mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
        mouse.click()
        print("화면 클릭" + time.strftime("%H:%M", time.localtime()))
        time.sleep(88)
        mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
        mouse.click()
        print("화면 클릭" + time.strftime("%H:%M", time.localtime()))    
        time.sleep(30)

        # on()
        # return

        select()
        keyboard.press_and_release('g')   # AUTO
        time.sleep(1)
        return
        



    
    scr = pyautogui.screenshot(region=(left + int(width*0.53), top + int(height*0.83), int(width*0.1), int(height*0.05)))
    scr.save("scr_odin_jang7.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)

    if results and results[0][1][:1] in ['마', '아']:   # 마을에서 부활
        print(results[0][1])
        mouse.move(int(left + (width * 0.57)), int(top + (height * 0.86)), absolute=True, duration=0.1)   # 확인
        mouse.click()
        time.sleep(15)
        flag_bok = True
        


    if flag_bok:
        print('flag_bok')

        mouse.move(left+(width*0.238), top+(height*0.1), absolute=True, duration=0.1)   # 복구
        mouse.click()
        time.sleep(1)
        
        mouse.move(left+(width*0.5), top+(height*0.37), absolute=True, duration=0.1)   # 복구
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.6), top+(height*0.77), absolute=True, duration=0.1)   # 무료복구
        mouse.click()
        time.sleep(1)

        keyboard.press_and_release('4')   # 잡화상
        time.sleep(20)

        mouse.move(left+(width*0.15), top+(height*0.23), absolute=True, duration=0.1)   # 중형회복물약
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.58), top+(height*0.6), absolute=True, duration=0.1)   # 최대
        mouse.click()
        time.sleep(1)
        
        mouse.move(left+(width*0.55), top+(height*0.73), absolute=True, duration=0.1)   # 구매하기
        mouse.click()
        time.sleep(1)

        keyboard.press_and_release('esc')   # 상점 나가기
        time.sleep(2)

        mouse.move(left+(width*0.021), top+(height*0.26), absolute=True, duration=0.1)   # 은총의순간
        mouse.click()
        time.sleep(5)

        mouse.move(left+(width*0.238), top+(height*0.357), absolute=True, duration=0.1)   # 동부황무지
        mouse.click()
        time.sleep(15)

        keyboard.press_and_release('g')   # AUTO
        time.sleep(1)


    return




















def a03_jangbi(play = 'dungeon'):
    print("오딘 a03_jangbi   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    

    mouse.move(left+(width*0.91), top+(height*0.09), absolute=True, duration=0.1)   # 가방
    mouse.click()
    time.sleep(8)

    mouse.move(left+(width*0.77), top+(height*0.93), absolute=True, duration=0.1)   # 일괄분해
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.95), top+(height*0.93), absolute=True, duration=0.1)   # 분해
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.57), top+(height*0.7), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.96), top+(height*0.3), absolute=True, duration=0.1)   # 업적
    mouse.click()
    time.sleep(3)

    mouse.move(left+(width*0.95), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.5), top+(height*0.95), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(1)
    
    mouse.move(left+(width*0.95), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)
    mouse.move(left+(width*0.5), top+(height*0.95), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    time.sleep(7)
        

    mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)
    
    mouse.move(left+(width*0.77), top+(height*0.77), absolute=True, duration=0.1)   # 우편함
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.95), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.55), top+(height*0.63), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.55), top+(height*0.88), absolute=True, duration=0.1)   # 화면클릭
    mouse.click()
    time.sleep(3)


    mouse.move(left+(width*0.23), top+(height*0.15), absolute=True, duration=0.1)   # 계정우편
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.95), top+(height*0.95), absolute=True, duration=0.1)   # 모두받기
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.55), top+(height*0.63), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.55), top+(height*0.88), absolute=True, duration=0.1)   # 화면클릭
    mouse.click()
    time.sleep(3)    


    mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)

    if play == 'play':
        mouse.move(left+(width*0.03), top+(height*0.53), absolute=True, duration=0.1)   # 절전
        mouse.click()
        
    return






def a04_dungeon(dungeon=2):
    print("오딘 a04_dungeon   " + time.strftime("%H:%M", time.localtime()))

    global left, top, width, height

    mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    mouse.move(left+(width*0.757), top+(height*0.538), absolute=True, duration=0.1)   # 던전
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.2), top+(height*0.15), absolute=True, duration=0.1)   # 정예던전
    mouse.click()
    time.sleep(3)

    if dungeon == 1:
        mouse.move(left+(width*0.88), top+(height*0.5), absolute=True, duration=0.1)   # 1공허의유적
        mouse.click()
        time.sleep(1)
        mouse.move(left+(width*0.88), top+(height*0.93), absolute=True, duration=0.1)   # 이동
        mouse.click()
        time.sleep(50)
        keyboard.press('w')
        time.sleep(8)
        keyboard.release('w')

    if dungeon == 2:  
        mouse.move(left+(width*0.88), top+(height*0.5), absolute=True, duration=0.1)   # 2난쟁이비밀통로
        mouse.press()
        time.sleep(1)
        mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.5)
        time.sleep(1)
        mouse.release()
        mouse.move(left+(width*0.88), top+(height*0.5), absolute=True, duration=0.1)
        mouse.click()
        time.sleep(1)
        mouse.move(left+(width*0.88), top+(height*0.93), absolute=True, duration=0.1)   # 이동
        mouse.click()
        time.sleep(50)
        keyboard.press('w')
        time.sleep(15)
        keyboard.release('w')

    if dungeon == 3:
        mouse.move(left+(width*0.88), top+(height*0.5), absolute=True, duration=0.1)   # 3지하감옥
        mouse.press()
        time.sleep(1)
        mouse.move(left+(width*0.3), top+(height*0.5), absolute=True, duration=0.5)
        time.sleep(1)
        mouse.release()

        mouse.move(left+(width*0.88), top+(height*0.5), absolute=True, duration=0.1)   # 3지하감옥
        mouse.press()
        time.sleep(1)
        mouse.move(left+(width*0.3), top+(height*0.5), absolute=True, duration=0.5)
        time.sleep(1)
        mouse.release()
        
        mouse.move(left+(width*0.88), top+(height*0.5), absolute=True, duration=0.1)
        mouse.click()
        time.sleep(1)
        mouse.move(left+(width*0.88), top+(height*0.93), absolute=True, duration=0.1)   # 이동
        mouse.click()
        time.sleep(50)
        keyboard.press('w')
        time.sleep(20)
        keyboard.release('w')
    
    keyboard.press_and_release('g')
    time.sleep(1)


    mouse.move(left+(width*0.03), top+(height*0.53), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(1)


    scr = pyautogui.screenshot(region=(left + int(width*0.08), top + int(height*0.17), int(width*0.1), int(height*0.07)))
    scr.save("scr_odin_dungeon.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr))
    print(results)


    global github_results, github_dungeon

    if results:
        github_results = results[0][1]
        github_dungeon = dungeon
        print(github_results)
        print(github_dungeon)

    else:
        github_results = 'No'
        github_dungeon = 0

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
    print("오딘 on   " + time.strftime("%H:%M", time.localtime()))

    for t in gw.getAllTitles():
        if "ODIN" in t:   # 제목에 'ODIN' 포함된 경우
            win = gw.getWindowsWithTitle(t)[0]
            win.close()
            time.sleep(1)
            app = Application().connect(handle=win._hWnd)
            app.window(handle=win._hWnd).set_focus()
            time.sleep(1)
            mouse.move(win.left+(win.width*0.55), win.top+(win.height*0.63), absolute=True, duration=0.1)   # 모두받기
            mouse.click()
            time.sleep(1)
            break



    # 크롬 로그인
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.Popen([chrome_path, "https://accounts.kakao.com/login/?continue=https%3A%2F%2Fodin.game.daum.net%2Fodin%2F#login"])

    keyboard.press_and_release('win + up')
    time.sleep(1)
    keyboard.press_and_release('tab')
    keyboard.write('s070092@nate.com')
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    keyboard.write('github01!')
    keyboard.press_and_release('enter')
    time.sleep(8)

    screen_width, screen_height = pyautogui.size()
    mouse.move(int(screen_width * 0.88), int(screen_height * 0.21), absolute=True, duration=0.1)   # 게임 실행
    mouse.click()
    time.sleep(8)
    mouse.move(int(screen_width * 0.1), int(screen_height * 0.45), absolute=True, duration=0.1)   # 지정PC 확인
    mouse.click()
    time.sleep(10)
    mouse.move(int(screen_width * 0.1), int(screen_height * 0.35), absolute=True, duration=0.1)   # 확인
    mouse.click()
    time.sleep(230)



    win = gw.getWindowsWithTitle('ODIN')[0]
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

    # 오딘 창
    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    print("화면 클릭" + time.strftime("%H:%M", time.localtime()))
    time.sleep(88)
    mouse.move(left+(width*0.5), top+(height*0.5), absolute=True, duration=0.1)   # 화면 클릭
    mouse.click()
    print("화면 클릭" + time.strftime("%H:%M", time.localtime()))    
    time.sleep(30)

    select(0)    # 캐릭터 선택
    a02_bok()   # 장시간 체크

    return









def select(character = 1):
    print("오딘 select   " + time.strftime("%H:%M", time.localtime()))


    global left, top, width, height

    time.sleep(3)

    if character != 0:
        mouse.move(left+(width*0.96), top+(height*0.09), absolute=True, duration=0.1)   # 메뉴
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.83), top+(height*0.77), absolute=True, duration=0.1)   # 캐릭터변경
        mouse.click()
        time.sleep(1)

        mouse.move(left+(width*0.57), top+(height*0.63), absolute=True, duration=0.1)   # 확인
        mouse.click()
        time.sleep(10)
    

    if character in [1, 0]:    
        mouse.move(left+(width*0.87), top+(height*0.2), absolute=True, duration=0.1)   # 1번 캐릭터
        mouse.click()
        time.sleep(1)

    if character == 2:
        mouse.move(left+(width*0.87), top+(height*0.33), absolute=True, duration=0.1)   # 2번 캐릭터
        mouse.click()
        time.sleep(1)

    if character == 3:
        mouse.move(left+(width*0.87), top+(height*0.43), absolute=True, duration=0.1)   # 3번 캐릭터
        mouse.click()
        time.sleep(1)

    if character == 4:
        mouse.move(left+(width*0.87), top+(height*0.55), absolute=True, duration=0.1)   # 4번 캐릭터
        mouse.click()
        time.sleep(1)

    if character == 5:
        mouse.move(left+(width*0.87), top+(height*0.65), absolute=True, duration=0.1)   # 5번 캐릭터
        mouse.click()
        time.sleep(1)



    mouse.move(left+(width*0.87), top+(height*0.91), absolute=True, duration=0.1)   # 게임하기
    mouse.click()

    global github_character
    github_character = character
    
    time.sleep(250)
    
    return




















def dungeon(character = 1, dungeon=2):
    a01_start()
    a02_bok()
    a03_jangbi()
    time.sleep(10)
    select(character)
    a04_dungeon(dungeon)
    github()

    return


def play():

    a01_start()
    a02_bok()
    a03_jangbi('play')

    return


    



if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        elif sys.argv[1] == "off":
            off()            
        elif sys.argv[1] == "dungeon":
            dungeon(int(sys.argv[2]), int(sys.argv[3]))
            
        elif sys.argv[1] == "github":
            github()
        else:
            play()
    else:
        play()












    
