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




def p01_start():
    print("조선협객전 p01_start   " + time.strftime("%H:%M", time.localtime()))

    if gw.getWindowsWithTitle('Chosun2M'):
        win = gw.getWindowsWithTitle('Chosun2M')[0]
    else:
        on()
        return

    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height






def p02_bok():
    print("조선협객전 p02_bok   " + time.strftime("%H:%M", time.localtime()))
    

    global left, top, width, height


    pyautogui.moveTo(left+(width*0.47), top+(height*0.85), 2.0)   # 절전 해제
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left+(width*0.57), top+(height*0.85), 2.0)
    pyautogui.mouseUp()

    time.sleep(3)



    scr_check01 = pyautogui.screenshot(region=(left, top+(height-20), 10, 10))
    scr_check01_np = np.array(scr_check01)
    hsv = cv2.cvtColor(scr_check01_np, cv2.COLOR_RGB2HSV)

    # 빨간색 픽셀 탐지
    mask = cv2.bitwise_or(
        cv2.inRange(hsv, np.array([0, 50, 50]), np.array([10, 255, 255])),
        cv2.inRange(hsv, np.array([170, 50, 50]), np.array([180, 255, 255]))
    )

    if np.any(mask):
        print("빨간색 계열이 발견되었습니다.")

        pyautogui.moveTo(left+(width*0.478), top+(height*0.88), 2.0) # 부활하기

        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        time.sleep(20)
    else:
        time.sleep(3)

    


    # 복구 확인 (개경 마을)
    scr_bok = pyautogui.screenshot(region=(left+int(width*0.838), top+int(height*0.35), int(width*0.07), int(height*0.038)))
    scr_bok_np = np.array(scr_bok)
    scr_bok.save("scr_jo_ge.png")

    reader = easyocr.Reader(['ko', 'en'], gpu=False)
    results = reader.readtext(scr_bok_np)

    print(results)



    if (results and ("개" in results[0][1] or "경" in results[0][1] or "마을" in results[0][1])):
        
        print("복구 개경 마을")


        # 복구
        pyautogui.moveTo(left+(width*0.72), top+(height*0.07), 2.0) # 복구
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        

        pyautogui.moveTo(left+(width*0.17), top+(height*0.9), 2.0) # 복구
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()
        
        pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.17), top+(height*0.9), 2.0) # 복구
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼        
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()


        time.sleep(1)

        pyautogui.press('esc')


        pyautogui.moveTo(left+(width*0.5), top+(height*0.25), 2.0) # 화면 클릭
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()




        

        pyautogui.moveTo(left+(width*0.238), top+(height*0.087), 2.0) # 체력        
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()


        pyautogui.moveTo(left+(width*0.2888), top+(height*0.087), 1.0) # 도력        
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        time.sleep(3)


        flag_che = False
        flag_do = False

        


        print("체력이 충분한지 그래픽 체크")

        scr_energy = pyautogui.screenshot(region=(left+int(width*0.2417), top+int(height*0.108), 3, 8))
        scr_energy_np = np.array(scr_energy)
        scr_energy.save("scr_jo_che.png")

        if np.any(np.all(scr_energy_np >= 100, axis=-1)): # 흰색이 있으면
            flag_che = True
        else:                                             # 흰색이 없으면
            flag_che = False

        print(flag_che)


        



        print("도력이 충분한지 그래픽 체크")
        scr_energy = pyautogui.screenshot(region=(left+int(width*0.2887), top+int(height*0.108), 3, 8))
        scr_energy_np = np.array(scr_energy)
        scr_energy.save("scr_jo_do.png")

        if np.any(np.all(scr_energy_np >= 100, axis=-1)): # 흰색이 있으면
            flag_do = True
        else:                                             # 흰색이 없으면
            flag_do = False

        print(flag_do)

        


        pyautogui.moveTo(left+(width*0.2388), top+(height*0.087), 2.0) # 체력        
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.2888), top+(height*0.087), 1.0) # 도력        
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()




        ###
        # 체력   도력 < 100
        ###


        if not flag_che or not flag_do:   # 체력, 도력이 100보다 작으면 (체력, 도력 그래픽 확인)
            #잡화상인에게 이동


 
            pyautogui.moveTo(left+(width*0.81), top+(height*0.25), 2.0) # 지도
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            
            pyautogui.moveTo(left+(width*0.80), top+(height*0.25), 2.0) # 개경 마을
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(2)
            

            pyautogui.moveTo(left+(width*0.80), top+(height*0.37), 2.0) # 잡화 상인
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(1)


            time.sleep(0.1)

            pyautogui.moveTo(left+(width*0.80), top+(height*0.95), 2.0) # 이동 버튼
            pyautogui.mouseDown()
            time.sleep(0.1)
            pyautogui.mouseUp()
            time.sleep(15)
            


            # 잡화상인 선택
            scr_heal = pyautogui.screenshot(region=(left+int(width*0.23), top+int(height*0.23), int(width*0.5), int(height*0.7)))
            scr_heal_np = np.array(scr_heal)
            scr_heal.save("scr_heal.png")


            # OCR 객체 생성 및 텍스트 추출
            reader = easyocr.Reader(['ko', 'en'], gpu=False)
            results = reader.readtext(scr_heal_np)

            str_heal = ""
            x_heal = 0
            y_heal = 0

            # 텍스트와 중심 좌표 출력
            print("OCR 텍스트 및 좌표:")
            for detection in results:
                bbox, text, confidence = detection
                top_left = bbox[0]
                bottom_right = bbox[2]
                x = (top_left[0] + bottom_right[0]) // 2
                y = (top_left[1] + bottom_right[1]) // 2
                print(f"{text} [{x}, {y}]")

                if "[" in text or "]" in text or "잡화" in text or "집화" in text:
                    str_heal = text
                    x_heal = x
                    y_heal = y
                    break


            print(str_heal)
            print(map(str_heal.find, "[잡집]"))


            str_heal_min = min([x for x in [str_heal.find("집"), str_heal.find("잡")] if x != -1], default=-1)

            
            print(str_heal_min)
            print((str_heal_min+1)*10 / len(str_heal))

            if len(str_heal) > 7 and (str_heal_min+1)*10 / len(str_heal) < 3.8:      # [잡화 상인] ???
                x_heal = x_heal - int(len(str_heal)/7) - 50
                
            elif len(str_heal) > 7 and (str_heal_min+1)*10 / len(str_heal) > 7:   # ??? [잡화 상인]
                x_heal = x_heal - int(len(str_heal)/7) + 5
                
            else:
                x_heal = x_heal - int(len(str_heal)/7)

            pyautogui.moveTo(left+int(width*0.25) + x_heal, top+int(height*0.26) + y_heal + int(height*0.07), 2.0)   # 잡화 상인
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()

            pyautogui.moveTo(left+(width*0.33), top+(height*0.85), 2.0)   # 상점 이용
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()
            time.sleep(2)


            # 체력, 도력 회복제 구매
            pyautogui.moveTo(left+(width*0.17), top+(height*0.70), 2.0)   # 상품
            pyautogui.mouseDown()
            time.sleep(1)

            pyautogui.moveTo(left+(width*0.17), top+(height*0.38), 2.0)   # 상품
            pyautogui.mouseUp()


            # 체력 회복제 구매
            if not flag_che:
                print("체력 회복제 구매")
                time.sleep(2)
                pyautogui.moveTo(left+(width*0.20), top+(height*0.615), 2.0)   # 체력 회복제
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()

                pyautogui.moveTo(left+(width*0.58), top+(height*0.80), 2.0)   # 구매
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()


                pyautogui.moveTo(left+(width*0.58), top+(height*0.73), 2.0)   # +1000
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()


                pyautogui.moveTo(left+(width*0.55), top+(height*0.83), 2.0)   # 확인
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()
                


            # 도력 회복제 구매
            if not flag_do:
                print("도력 회복제 구매")                
                time.sleep(2)
                pyautogui.moveTo(left+(width*0.17), top+(height*0.80), 2.0)   # 상품
                pyautogui.mouseDown()
                time.sleep(1)

                pyautogui.moveTo(left+(width*0.17), top+(height*0.30), 2.0)   # 상품
                pyautogui.mouseUp()

                pyautogui.moveTo(left+(width*0.20), top+(height*0.678), 2.0)   # 도력 회복제
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()

                pyautogui.moveTo(left+(width*0.58), top+(height*0.80), 2.0)   # 구매
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()

                pyautogui.moveTo(left+(width*0.58), top+(height*0.73), 2.0)   # +1000
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()


                pyautogui.moveTo(left+(width*0.55), top+(height*0.83), 2.0)   # 확인
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()


            pyautogui.moveTo(left+(width*0.55), top+(height*0.93), 2.0)   # 구매
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()

            pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼
            pyautogui.mouseDown()
            time.sleep(0.3)
            pyautogui.mouseUp()





            # 상점 진입 확인 (개경 마을)
            scr_shop = pyautogui.screenshot(region=(left+int(width*0.11), top+int(height*0.15), int(width*0.1), int(height*0.1)))
            scr_shop_np = np.array(scr_shop)
            scr_shop.save("scr_jo_shop.png")

            reader = easyocr.Reader(['ko', 'en'], gpu=False)
            results = reader.readtext(scr_shop_np)
            print(results)

            if results and results[0][1][0] == "상":
                pyautogui.moveTo(left+(width*0.95), top+(height*0.07), 2.0) # 종료
                pyautogui.mouseDown()
                time.sleep(0.5)
                pyautogui.mouseUp()
        



        print("이동")
        # 사냥도감
        pyautogui.moveTo(left+(width*0.95), top+(height*0.07), 2.0) # 메뉴
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.95), top+(height*0.18), 2.0) # 사냥도감
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        time.sleep(5)

        pyautogui.moveTo(left+(width*0.055), top+(height*0.43), 3.0) # 요도우라   36  46  56  63  70  78
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.17), top+(height*0.33), 2.0) # 맷돼지
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.91), top+(height*0.95), 2.0) # 이동
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()

        time.sleep(20)

        time.sleep(3)
        pyautogui.moveTo(left+(width*0.915), top+(height*0.73), 2.0) # AUTO 버튼
        pyautogui.mouseDown()
        time.sleep(0.3)
        pyautogui.mouseUp()




def p03_jangbi():
    print("조선협객전 p03_jangbi   " + time.strftime("%H:%M", time.localtime()))
    

    global left, top, width, height





    # 장비 도감
    pyautogui.moveTo(left+(width*0.958), top+(height*0.07), 2.0) # 메뉴
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.767), top+(height*0.28), 2.0) # 장비도감
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(2)

    pyautogui.moveTo(left+(width*0.838), top+(height*0.93), 2.0) # 장비도감 일괄등록
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.577), top+(height*0.65), 2.0) # 확인 버튼
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(3.0)

    
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.967), top+(height*0.08), 2.0) # 장비도감 종료
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()







    # 가방 분해
    pyautogui.moveTo(left+(width*0.957), top+(height*0.07), 2.0) # 메뉴

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.81), top+(height*0.08), 2.0) # 가방

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




    pyautogui.moveTo(left+(width*0.757), top+(height*0.18), 2.0) # 장비

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.95), top+(height*0.76), 2.0) # 장비선택
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.638), top+(height*0.23), 5.0) # 쓰레기통
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.56), top+(height*0.67), 2.0) # 삭제버튼
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.95), top+(height*0.76), 2.0) # 장비선택
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.638), top+(height*0.23), 5.0) # 쓰레기통
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.56), top+(height*0.67), 2.0) # 삭제버튼
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    




    pyautogui.moveTo(left+(width*0.81), top+(height*0.917), 2.0) # 분해

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.417), top+(height*0.638), 2.0) # 장비

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.417), top+(height*0.68), 2.0) # 일반

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.47), top+(height*0.68), 2.0) # 고급

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.81), 2.0) # 분해버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    


    pyautogui.moveTo(left+(width*0.56), top+(height*0.638), 2.0) # 확인버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    
    pyautogui.moveTo(left+(width*0.50), top+(height*0.67), 2.0) # 확인버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.388), top+(height*0.81), 2.0) # 취소버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.288), top+(height*0.167), 2.3) # X버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.038), top+(height*0.763), 2.3) # 절전

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    # time.sleep(3)
    # pyautogui.screenshot(region=(left, top, width, height)).save('jo.png')
    













def on():
    print("조선협객전 on   " + time.strftime("%H:%M", time.localtime()))

    if gw.getWindowsWithTitle('Chosun2M'):
        os.system("taskkill /F /IM _gins321.exe")
    
          
    desktop = os.environ.get('COMPUTERNAME')

    if desktop in ["DESKTOP-LRGAL8H"]:
        subprocess.Popen(r"D:\Program Files\Chosun2M\Chosun2M.exe", shell=True)  # 프로그램 실행
    else:
        subprocess.Popen(r"C:\Program Files\Chosun2M\Chosun2M.exe", shell=True)  # 프로그램 실행


    time.sleep(15)

    """
    if desktop in ["DESKTOP-MA2NLC4"]:
        if gw.getWindowsWithTitle('Chosun2M'):
            os.system("taskkill /F /IM _gins321.exe")
        os.system("taskkill /F /IM Chosun2M.exe")
        time.sleep(10)        
        subprocess.Popen(r"C:\Program Files\Chosun2M\Chosun2M.exe", shell=True)  # 프로그램 실행
        time.sleep(15)
    """



        
    

    for i in range(18):
        print("조선협객전을 오픈 합니다. " + str(i+1))
        if gw.getWindowsWithTitle('Chosun2M'):
            break
        time.sleep(10)
            
        
    win = gw.getWindowsWithTitle('Chosun2M')[0]
    print("조선협객전 오픈 완료")



    
    time.sleep(0.1)

    """
    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()
    """



    try:
        time.sleep(5)
        print(8)
        app = Application().connect(handle=win._hWnd)
    except Exception as e:
        try:
            time.sleep(5)
            print(8)
            app = Application().connect(handle=win._hWnd)
        except Exception as e:
            try:
                time.sleep(5)
                print(8)
                app = Application().connect(handle=win._hWnd)
            except Exception as e:
                try:
                    time.sleep(5)
                    print(8)
                    app = Application().connect(handle=win._hWnd)
                except Exception as e:
                    try:
                        time.sleep(5)
                        print(8)
                        app = Application().connect(handle=win._hWnd)
                    except Exception as e:
                        print(e)


    try:
        time.sleep(5)
        print(8)
        app.window(handle=win._hWnd).set_focus()
    except Exception as e:
        try:
            time.sleep(5)
            print(8)
            app.window(handle=win._hWnd).set_focus()
        except Exception as e:
            try:
                time.sleep(5)
                print(8)
                app.window(handle=win._hWnd).set_focus()
            except Exception as e:
                try:
                    time.sleep(5)
                    print(8)
                    app.window(handle=win._hWnd).set_focus()
                except Exception as e:
                    try:
                        time.sleep(5)
                        print(8)
                        app.window(handle=win._hWnd).set_focus()
                    except Exception as e:
                        print(e)









    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height

    time.sleep(120)

    try:
        pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
    except Exception as e:
        try:
            time.sleep(3)
            pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
        except Exception as e:
            try:
                time.sleep(3)
                pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
            except Exception as e:
                try:
                    time.sleep(3)
                    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
                except Exception as e:
                    try:
                        time.sleep(3)
                        pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)
                    except Exception as e:
                        print(e)
                        on()

        
    
    pyautogui.moveTo(left+(width*0.5), top+(height*0.5), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    time.sleep(38)

    pyautogui.moveTo(left+(width*0.6), top+(height*0.5), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    

    pyautogui.moveTo(left+(width*0.5), top+(height*0.6), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()    


    pyautogui.moveTo(left+(width*0.6), top+(height*0.7), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

    pyautogui.moveTo(left+(width*0.5), top+(height*0.7), 2.0)   # 화면 클릭
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    
    time.sleep(3)


    
    # 케릭터 선택
    pyautogui.moveTo(left+(width*0.83), top+(height*0.91), 2.0)   # 게임 시작
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


    time.sleep(50)


    # 미션 건너뛰기
    pyautogui.moveTo(left+(width*0.89), top+(height*0.63), 2.0)   # 건너뛰기
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(5)
    
    pyautogui.moveTo(left+(width*0.38), top+(height*0.91), 2.0)   # 취소
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    time.sleep(5)

    pyautogui.moveTo(left+(width*0.915), top+(height*0.73), 2.0) # AUTO 버튼
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()



    p02_bok()

    time.sleep(3)

    p03_jangbi()






















def play_jo():
    try:
        p01_start()
    except Exception as e:
        print(f"조선협객전 p01_start 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        p02_bok()
    except Exception as e:
        print(f"조선협객전 p02_bok 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")


    try:
        p03_jangbi()
    except Exception as e:
        print(f"조선협객전 p03_jangbi 오류 {time.strftime('%H:%M', time.localtime())}{'\n'}{e}")














    




if __name__ == "__main__":
    # play_jo()
    on()



