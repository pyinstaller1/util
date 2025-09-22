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
import sys
import keyboard, mouse
import pyperclip
from datetime import datetime




# left, top, width, height = 0, 0, 0, 0
che = 1000
app = None






def github():
    print("아래스 github01   " + time.strftime("%H:%M", time.localtime()))

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H"]:
        url = "https://github.com/pyinstaller1/game/edit/main/ares1.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        url = "https://github.com/pyinstaller1/game/edit/main/ares2.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        url = "https://github.com/pyinstaller1/game/edit/main/ares3.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        url = "https://github.com/pyinstaller1/game/edit/main/ares4.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
        url = "https://github.com/pyinstaller1/game/edit/main/ares5.txt"

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-NT06800"]:
        url = "https://github.com/pyinstaller1/game/edit/main/ares6.txt"


    process = subprocess.Popen([chrome_path, "--new-window", "--start-maximized", "--force-device-scale-factor=1", url])   # 크롬 열기

    time.sleep(10)

    keyboard.press_and_release('win + up')
    time.sleep(3)

    win = gw.getWindowsWithTitle('Editing game/ares')[0]
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

    global str_location
    try:
        if str_location:
            pass
    except:
        str_location = '오류'

    
    # str_dungeon = "초원"

    
    now = now.strftime("%m%d %H:%M\t") + str_location + '\n'
    str_temp = now + str_temp
    print(str_temp)
    time.sleep(1)
    pyperclip.copy(str_temp)


    keyboard.press_and_release('ctrl + v')


    mouse.move(left+(width*0.95), top+(height*0.25), absolute=True, duration=0.1)   # 커밋
    mouse.click()

    time.sleep(1)

    keyboard.press_and_release('enter')

    time.sleep(8)



    for win in gw.getWindowsWithTitle('game/ares'):
        if win.title.strip():
            print(win.title.split(" - ")[0].split("·")[1].strip())
            win.close()
            break














def a01_start():
    print(7)



    print("아레스 a01_start   " + time.strftime("%H:%M", time.localtime()))



    if not gw.getWindowsWithTitle('아레스'):
        print("아레스 창이 없습니다.")
        on()
        return False


    """
    if len(gw.getWindowsWithTitle('아레스')) == 1:
        print("창이 1개만 있으므로 닫습니다.")
        on()
        return False
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

    pyautogui.moveTo(left+(width*0.5), top+(height*0.65), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.65), 2.0)
    pyautogui.mouseUp()

    return True













def a02_bok():
    print("아레스 a02_bok   " + time.strftime("%H:%M", time.localtime()))

    time.sleep(1)
    mouse.move(left+(width*0.028), top+(height*0.738), absolute=True, duration=0.1)   # 절전
    mouse.click()
    time.sleep(1)    

    global str_location
    str_location = "Bok일반"
    
    time.sleep(0.1)
    r, g, b = pyautogui.pixel(int(left+(width*0.5)), int(top+(height*0.5)))
    
    if (80 < r < 100) and (88 < g < 120) and (80 < b < 100):
        str_location = "Bok광장"
        print("광장")

        
    pyautogui.moveTo(left+(width*0.5), top+(height*0.65), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.7), top+(height*0.65), 2.0)
    pyautogui.mouseUp()
    time.sleep(3)

        


    if (80 < r < 100) and (88 < g < 120) and (80 < b < 100):
        print("광장")

        mouse.move(left+(width*0.178), top+(height*0.12), absolute=True, duration=0.1)   # 복구
        mouse.click()
        time.sleep(2)

        mouse.move(left+(width*0.55), top+(height*0.73), absolute=True, duration=0.1)   # 확인
        mouse.click()
        time.sleep(2)


        mouse.right_click()
        time.sleep(1)

        mouse.move(left+(width*0.95), top+(height*0.83), absolute=True, duration=0.1)   # 잡화상인
        mouse.click()
        time.sleep(1)

        mouse.right_click()

        time.sleep(15)

        mouse.move(left+(width*0.9), top+(height*0.95), absolute=True, duration=0.1)   # 구매
        mouse.click()
        time.sleep(2)

        mouse.move(left+(width*0.56), top+(height*0.56), absolute=True, duration=0.1)   # MAX
        mouse.click()
        time.sleep(2)
        
        mouse.move(left+(width*0.57), top+(height*0.71), absolute=True, duration=0.1)   # 확인
        mouse.click()
        time.sleep(2)







        mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
        mouse.click()
        time.sleep(5)

        mouse.move(left+(width*0.07), top+(height*0.17), absolute=True, duration=0.1)   # 지도
        mouse.click()
        time.sleep(7)


        mouse.move(left+(width*0.07), top+(height*0.17), absolute=True, duration=0.1)   # 복구
        mouse.click()
        time.sleep(3)

        mouse.move(left+(width*0.03), top+(height*0.95), absolute=True, duration=0.1)   # 행성지도
        mouse.click()
        time.sleep(2)

        mouse.move(left+(width*0.80), top+(height*0.43), absolute=True, duration=0.1)   # 무어랜드
        mouse.click()
        time.sleep(2)







        # 지도 ocr 탐지
        scr = pyautogui.screenshot(region=(left + int(width*0.23), top + int(height*0.2), int(width*0.6), int(height*0.77)))
        scr.save("scr_ares_map.png")
        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(np.array(scr))
        print(results)


        print(7)


        list_map = []

        for item in results:
            if item[1][0] not in ['몬', '본', '온', '{', '생', '최'] or item[1][:1] not in ['미어', '마이']:
                print(item[1])

                x = (item[0][0][0] + item[0][1][0]) // 2
                y = (item[0][0][1] + item[0][2][1]) // 2
                list_temp = []
                list_temp.append(x)
                list_temp.append(y)
                list_map.append(list_temp)

        list_map_number = int(time.strftime("%S"))%len(list_map)



        pyautogui.moveTo(left + int(width*0.23) + list_map[list_map_number][0], top + int(height*0.2) + list_map[list_map_number][1] - int(height*0.03), 2.0)   # 지도
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        time.sleep(3)







        list_map = []
        # 자동 이동 ocr 탐지
        scr_auto = pyautogui.screenshot(region=(left + int(width*0.15), top + int(height*0.38), int(width*0.7), int(height*0.6)))
        scr_auto.save("scr_ares_auto.png")
        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(np.array(scr_auto))
        print(results)


        list_map = []
        for item in results:
            print(item)
            if len(item[1]) == 5 and item[1][:1]in ['자', '가', '지', '기']:
                x = (item[0][0][0] + item[0][1][0]) // 2
                y = (item[0][0][1] + item[0][2][1]) // 2
                list_temp = []
                list_temp.append(x)
                list_temp.append(y)
                list_map.append(list_temp)
                break

        print(list_map)

        pyautogui.moveTo(left + int(width*0.15) + list_map[0][0], top + int(height*0.38) + list_map[0][1], 2.0)   # 자동 이동
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        time.sleep(2)
        mouse.move(left+(width*0.57), top+(height*0.61), absolute=True, duration=0.1)   # 확인
        mouse.click()

        time.sleep(50)    

    return









def a03_jangbi():
    print("아레스 a03_jangbi   " + time.strftime("%H:%M", time.localtime()))

    time.sleep(1)

    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(2)
        
    mouse.move(left+(width*0.83), top+(height*0.43), absolute=True, duration=0.1)   # 거래소
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.27), top+(height*0.173), absolute=True, duration=0.1)   # 판매
    mouse.click()
    time.sleep(5)

    mouse.move(left+(width*0.27), top+(height*0.173), absolute=True, duration=0.1)   # 판매
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.77), top+(height*0.95), absolute=True, duration=0.1)   # 일괄재등록
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.58), top+(height*0.627), absolute=True, duration=0.1)   # 등록
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.61), top+(height*0.95), absolute=True, duration=0.1)   # 일괄정산
    mouse.click()
    time.sleep(2)

    mouse.move(left+(width*0.95), top+(height*0.95), absolute=True, duration=0.1)   # 등록 버튼
    mouse.click()
    time.sleep(2)




    # 거래소 판매 ocr 탐지
    scr_sell = pyautogui.screenshot(region=(left + int(width*0.32), top + int(height*0.25), int(width*0.17), int(height*0.08)))
    scr_sell_np = np.array(scr_sell)
    scr_sell.save("scr_ares_sell.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_sell_np)
    print(results)

    if results and ("원석" in results[0][1] or "결정" in results[0][1] or "에너지원" in results[0][1] or "설계도" in results[0][1] or "주괴" in results[0][1]):
        pyautogui.press('esc')
    else:
        pyautogui.moveTo(left+(width*0.58), top+(height*0.78), 2.0)   # 등록
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.58), top+(height*0.687), 1.0)   # 등록
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)








    # 모노리스 자동합성
    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)
    
    pyautogui.moveTo(left+(width*0.83), top+(height*0.37), 2.0)   # 모노리스
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(8)

    pyautogui.moveTo(left+(width*0.15), top+(height*0.157), 2.0)   # 합성
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(3)

    pyautogui.moveTo(left+(width*0.88), top+(height*0.95), 2.0)   # 자동합성
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.57), top+(height*0.60), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(25)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.95), 2.0)   # 나가기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)


    # 방어구 분해

    mouse.move(left+(width*0.93), top+(height*0.083), absolute=True, duration=0.1)   # 가방
    mouse.click()
    time.sleep(12)

    pyautogui.moveTo(left+(width*0.08), top+(height*0.23), 2.0)   # 방어구
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.7), top+(height*0.95), 2.0)   # 일괄분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.63), top+(height*0.23), 2.0)   # 선택
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.95), top+(height*0.95), 2.0)   # 일괄분해
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.57), top+(height*0.73), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 확인
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.6), 2.0)   # 화면 터치
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)








    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    




    print("거래소 완료")
    

    return





def a04_dungeon():
    print("아레스 던전   " + time.strftime("%H:%M", time.localtime()))



    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(3)



    pyautogui.moveTo(left+(width*0.1), top+(height*0.58), 3.0)   # 경쟁
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.38), top+(height*0.38), 2.0)   # 모리아기지
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)

    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    





    time.sleep(38)


    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(8)







    # 주간 던전 지도 ocr 탐지
    scr_dungeon = pyautogui.screenshot(region=(left + int(width*0.2), top + int(height*0.2), int(width*0.6), int(height*0.6)))
    scr_dungeon.save("scr_ares_dungeon.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr_dungeon))
    print(results)


    print(7)


    list_map = []
    for item in results:
        print(item)
        if 1==1: # len(item[1][:2]) >= 2 and item[1][:2]== '기지':
            x = (item[0][0][0] + item[0][1][0]) // 2
            y = (item[0][0][1] + item[0][2][1]) // 2
            list_temp = []
            list_temp.append(x)
            list_temp.append(y)
            list_map.append(list_temp)


    list_map_number = int(time.strftime("%S"))%(len(list_map))



    pyautogui.moveTo(left + int(width*0.2) + list_map[list_map_number][0], top + int(height*0.2) + list_map[list_map_number][1] - int(height*0.03), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left + int(width*0.2) + list_map[list_map_number][0], top + int(height*0.2) + list_map[list_map_number][1] - int(height*0.03), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left + int(width*0.2) + list_map[list_map_number][0], top + int(height*0.2) + list_map[list_map_number][1] - int(height*0.03), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(15)



    # 자동 이동 ocr 탐지
    scr_auto = pyautogui.screenshot(region=(left + int(width*0.15), top + int(height*0.38), int(width*0.7), int(height*0.6)))
    scr_auto.save("scr_ares_auto.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr_auto))
    print(results)


    list_map = []
    for item in results:
        print(item)
        if len(item[1]) == 5 and item[1][:1]in ['자', '가', '지', '기']:
            x = (item[0][0][0] + item[0][1][0]) // 2
            y = (item[0][0][1] + item[0][2][1]) // 2
            list_temp = []
            list_temp.append(x)
            list_temp.append(y)
            list_map.append(list_temp)
            break

    print(list_map)



    pyautogui.moveTo(left + int(width*0.15) + list_map[0][0], top + int(height*0.38) + list_map[0][1], 2.0)   # 자동 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left + int(width*0.15) + list_map[0][0], top + int(height*0.38) + list_map[0][1], 2.0)   # 자동 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()





    time.sleep(5)





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



    pyautogui.moveTo(left+(width*0.5), top+(height*0.88), 2.0)   # 빈칸
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)



    ### 우편

    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)


    pyautogui.moveTo(left+(width*0.838), top+(height*0.63), 2.0)   # 우편
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)

    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 계정 우편함
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.75), top+(height*0.958), 2.0)   # 모두 받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.75), top+(height*0.958), 2.0)   # 모두 받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.75), top+(height*0.958), 2.0)   # 모두 받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()






    pyautogui.moveTo(left+(width*0.07), top+(height*0.23), 2.0)   # 캐릭터 우편함
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.75), top+(height*0.958), 2.0)   # 모두 받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.75), top+(height*0.958), 2.0)   # 모두 받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.75), top+(height*0.958), 2.0)   # 모두 받기
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 닫기
    mouse.click()
    time.sleep(1)

    

    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(3)
    scr_bok = pyautogui.screenshot(region=(left + int(width*0.006), top + int(height*0.1), int(width*0.1), int(height*0.2)))
    scr_bok.save("scr_ares_bok.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr_bok))
    print(results)

    global str_location    
    if results:
        str_location = 'Dungeon_week ' + results[0][1]
    else:
        str_location = 'Dungeon_week No'









def a05_dungeon_week():
    print("아레스 주간 던전   " + time.strftime("%H:%M", time.localtime()))


    mouse.move(left+(width*0.967), top+(height*0.083), absolute=True, duration=0.1)   # 메뉴
    mouse.click()
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.1), top+(height*0.58), 3.0)   # 경쟁
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(3)

    pyautogui.moveTo(left+(width*0.58), top+(height*0.38), 2.0)   # 타루크기지
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.9), top+(height*0.95), 2.0)   # 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(20)

    pyautogui.press('esc')
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.3), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(1)    


    pyautogui.moveTo(left+(width*0.07), top+(height*0.17), 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(5)



    # 주간 던전 지도 ocr 탐지
    scr_week = pyautogui.screenshot(region=(left + int(width*0.2), top + int(height*0.2), int(width*0.6), int(height*0.6)))
    scr_week_np = np.array(scr_week)
    scr_week.save("scr_ares_week.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_week_np)
    print(results)








    pyautogui.moveTo(left + int(width*0.2) + results[0][0][0][0] + 10, top + int(height*0.2) + results[0][0][0][1] - 10, 2.0)   # 지도
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()





    time.sleep(3)
    map_x = results[0][0][0][0]
    map_y = results[0][0][0][1]





    # 자동이동 ocr 탐지
    scr_move = pyautogui.screenshot(region=(int(left + int(width*0.2) + results[0][0][0][0]) + int(width*0.05), int(top + int(height*0.2) + results[0][0][0][1] + int(height*0.118)), int(width*0.1), int(height*0.1)))
    scr_move_np = np.array(scr_move)
    scr_move.save("scr_ares_move.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_move_np)
    print(results)



    pyautogui.moveTo(int(left + int(width*0.2) + results[0][0][0][0]) + int(width*0.05) + map_x + 10, int(top + int(height*0.2) + results[0][0][0][1] + int(height*0.118)) + map_y + 10, 2.0)   # 자동 이동
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(1)
    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()



    time.sleep(3)
    scr_bok = pyautogui.screenshot(region=(left + int(width*0.006), top + int(height*0.1), int(width*0.1), int(height*0.2)))
    scr_bok.save("scr_ares_bok.png")
    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(np.array(scr_bok))
    print(results)

    global str_location    
    if results:
        str_location = 'Dungeon_week ' + results[0][1]
    else:
        str_location = 'Dungeon_week No'


    return















def off():
    print("아레스 off   " + time.strftime("%H:%M", time.localtime()))
            

    if len(gw.getWindowsWithTitle('아레스')) == 2:
        win = gw.getWindowsWithTitle('아레스')[1]

        global left, top, width, height

        left = win.left
        top = win.top
        width = win.width
        height = win.height

        app = Application().connect(handle=win._hWnd)
        app.window(handle=win._hWnd).set_focus()

        time.sleep(1)



        pyautogui.moveTo(left+(width*0.99), top+(height*0.01), 1.0)   # 종료
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.5), top+(height*0.6), 2.0)   # 방치모드
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        

        time.sleep(7)
        scr_bang = pyautogui.screenshot(region=(left+int(width*0.3), top+int(height*0.3), int(width*0.5), int(height*0.5)))
        scr_bang_np = np.array(scr_bang)
        scr_bang.save("scr_ares_bang.png")

        reader = easyocr.Reader(['ko', 'en'], gpu=False)
        results = reader.readtext(scr_bang_np)
        print(results)

        for detection in results:
            if '방치' in detection[1]:
                bbox, text, confidence = detection
                top_left = bbox[0]
                bottom_right = bbox[2]
                x = (top_left[0] + bottom_right[0]) // 2
                y = (top_left[1] + bottom_right[1]) // 2
                print(f"{text} [{x}, {y}]")


                pyautogui.moveTo(left+int(width*0.3)+x, top+int(height*0.3)+y, 2.0)   # 방치모드
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()


                pyautogui.moveTo(left+int(width*0.55), top+int(height*0.75), 2.0)   # 방치모드
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()

                pyautogui.moveTo(left+int(width*0.55), top+int(height*0.61), 2.0)   # 방치모드
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()
                

    time.sleep(17)

    win = gw.getWindowsWithTitle('아레스')[0]

    # global left, top, width, height

    left = win.left
    top = win.top
    width = win.width
    height = win.height

    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()

    time.sleep(1)



    pyautogui.moveTo(left+(width*0.99), top+(height*0.01), 1.0)   # 종료
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.5), top+(height*0.6), 2.0)   # 방치모드
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
        

    time.sleep(7)
    scr_bang = pyautogui.screenshot(region=(left+int(width*0.3), top+int(height*0.3), int(width*0.5), int(height*0.5)))
    scr_bang_np = np.array(scr_bang)
    scr_bang.save("scr_ares_bang.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bang_np)
    print(results)


    for detection in results:
        if '방치' in detection[1]:
            bbox, text, confidence = detection
            top_left = bbox[0]
            bottom_right = bbox[2]
            x = (top_left[0] + bottom_right[0]) // 2
            y = (top_left[1] + bottom_right[1]) // 2
            print(f"{text} [{x}, {y}]")

            pyautogui.moveTo(left+int(width*0.3)+x, top+int(height*0.3)+y, 2.0)   # 방치모드
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()

            pyautogui.moveTo(left+int(width*0.55), top+int(height*0.75), 2.0)   # 방치모드
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()

            pyautogui.moveTo(left+int(width*0.55), top+int(height*0.61), 2.0)   # 방치모드
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()

                
    return





    










def on():
    print("아레스 on   " + time.strftime("%H:%M", time.localtime()))
            
    for proc in psutil.process_iter():
        if "Ares.exe" in proc.name():  # 프로세스 이름을 확인
            proc.kill()  # 강제 종료
            print("아레스 창을 닫았습니다.")
        if "ARES_Launcher.exe" in proc.name():  # 프로세스 이름을 확인
            proc.kill()  # 강제 종료
            print("ARES Launcher 창을 닫았습니다.")
                    


    time.sleep(1)


    if os.environ.get('COMPUTERNAME') == "DESKTOP-LRGAL8H":
        subprocess.Popen(r"D:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)
    else:
        subprocess.Popen(r"C:\Kakaogames\ARES\ARES_Launcher.exe", shell=True)

    print("ARES Launcher 오픈")

    time.sleep(50)




    win = gw.getWindowsWithTitle('ARES Launcher')[0]


    print(f"{win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")


    app_kakao = Application().connect(handle=win._hWnd)
    app_kakao.window(handle=win._hWnd).set_focus()



    time.sleep(3)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.5), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(1)


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.17), 2.0) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        pyautogui.write('ground077@naver.com')
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        pyautogui.write('ground077')
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        pyautogui.write('ground078')
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
        pyautogui.write('ground088')
        
    pyautogui.press("enter")
    

    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.3), 0.3) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    pyautogui.write('windows1!')
    pyautogui.press("enter")

    time.sleep(30)


    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]

    pyautogui.moveTo(win.left+(win.width*0.87), win.top+(win.height*0.78), 2.0) # 게임 실행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)


    for i in range(10):
        time.sleep(60)
        if gw.getWindowsWithTitle('아레스'):
            win = gw.getWindowsWithTitle('아레스')[0]
            break


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 점검 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)




    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()












    

    time.sleep(38)

    pyautogui.moveTo(left+(width*0.88), top+(height*0.738), 2.0)   # 게임 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)


    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)    

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)

    pyautogui.moveTo(left+(width*0.5), top+(height*0.3), 2.0)   # 이벤트 제거
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)    

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 이벤트 제거
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    
    time.sleep(10)

    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(20)

    pyautogui.press('g')   # AUTO
    

    # 복구 ocr 탐지
    scr_bok = pyautogui.screenshot(region=(left + int(width*0.006), top + int(height*0.1), int(width*0.1), int(height*0.2)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ares_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results[0][1])

    if results[0][1][0] in ["광", "대"]:
        a02_bok()


    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    

    time.sleep(1)







    
    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]   # 로그아웃
    app_kakao = Application().connect(handle=win._hWnd)
    app_kakao.window(handle=win._hWnd).set_focus()

    pyautogui.moveTo(win.left+(win.width*0.93), win.top+(win.height*0.08), 2.0)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')

    time.sleep(120)



    # [1] 시작
    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]
    app_kakao = Application().connect(handle=win._hWnd)
    app_kakao.window(handle=win._hWnd).set_focus()
    print("아레스[1] 시작")
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.5), 2.0) # 카카오 로그인
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(1)


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.17), 2.0) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-MA2NLC4"]:
        pyautogui.write('s0700921@nate.com')
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        pyautogui.write('s070092@nate.com')
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-OHGK5MV"]:
        pyautogui.write('s070092@kakao.com')
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-H9B70U0"]:
        pyautogui.write('s0700921@kakao.com')



    '''
    if os.environ.get('COMPUTERNAME') in ["DESKTOP-LRGAL8H", "DESKTOP-792RKKB"]:
        pyautogui.write('s070092@nate.com')
    else:
        pyautogui.write('s0700921@nate.com')
    pyautogui.press("enter")
    '''
    

    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.3), 0.3) # 입력
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    if os.environ.get('COMPUTERNAME') in ["DESKTOP-792RKKB"]:
        pyautogui.write('github01!')
    else:
        pyautogui.write('windows1!')
    pyautogui.press("enter")

    time.sleep(50)


    win = gw.getWindowsWithTitle('ARES Launcher')[len(gw.getWindowsWithTitle('ARES Launcher'))-1]

    time.sleep(1)
    
    pyautogui.moveTo(win.left+(win.width*0.87), win.top+(win.height*0.78), 2.0) # 게임 실행
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(10)



    for i in range(10):
        time.sleep(60)
        if gw.getWindowsWithTitle('아레스'):
            win = gw.getWindowsWithTitle('아레스')[0]
            break
        
    left = win.left
    top = win.top
    width = win.width
    height = win.height


    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 점검 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)




    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(1)
    
    pyautogui.moveTo(win.left+(win.width*0.5), win.top+(win.height*0.6), 2.0) # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(10)

    pyautogui.moveTo(left+(width*0.88), top+(height*0.738), 2.0)   # 게임 입장
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(30)


    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)    

    pyautogui.press('esc')   # 이벤트 제거
    time.sleep(1)
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 이벤트 제거
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    
    
    time.sleep(10)

    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(20)

    pyautogui.press('g')   # AUTO
    

    # 복구 ocr 탐지
    scr_bok = pyautogui.screenshot(region=(left + int(width*0.006), top + int(height*0.1), int(width*0.1), int(height*0.2)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_ares_bok.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)
    print(results[0][1])

    if results[0][1][0] in ["광", "대"]:
        a02_bok()




    pyautogui.moveTo(left+(width*0.0278), top+(height*0.738), 2.0)   # 절전
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    


    
    return















def dungeon_week():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    try:
        a05_dungeon_week()
    except Exception as e:
        print(f"아레스  a05_dungeon_week() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    github()

    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    try:
         a05_dungeon_week()
    except Exception as e:
        print(f"아레스  a05_dungeon_week() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    github()






def dungeon():
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    try:
        a04_dungeon()
    except Exception as e:
        print(f"아레스  a04_dungeon() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")
    github()


    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    try:
        a04_dungeon()
    except Exception as e:
        print(f"아레스  a04_dungeon() 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    github()











    
def play():
    
    try:
        if not a01_start():
            return
    except Exception as e:
        print(f"아레스 a01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")



    try:
        a02_bok()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")


    try:
        a03_jangbi()
    except Exception as e:
        print(f"아레스 a03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    github()


    try:
        if not a01_start1():
            return
    except Exception as e:
        print(f"아레스 a01_start[1] 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    try:
        a02_bok()
    except Exception as e:
        print(f"아레스 a02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    try:
        a03_jangbi()
    except Exception as e:
        print(f"아레스 a03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}")

    github()














if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "on":
            on()
        elif sys.argv[1] == "dungeon":
            dungeon()
        elif sys.argv[1] == "dungeon_week":
            dungeon_week()            
        else:
            play()
    else:
        play()
        # on()
        # mission()
        # off()












    
