

import on, ares, rf, vp
import time
import numpy as np
import keyboard
import os
from pynput.mouse import Controller, Button
import datetime


# "DESKTOP-LRGAL8H"
# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-H9B70U0"
# "DESKTOP-NT06800"


# 아레스 매일 오전 5시 dal.play_dal("던전0")




def get_log(text=''):
    filename = "log_total.txt"
    # 파일이 없으면 빈 파일 생성
    if not os.path.exists(filename):
        open(filename, "w", encoding="utf-8").close()
    with open(filename, "r+", encoding="utf-8") as f:
        original_text = f.read()
        f.seek(0)
        f.write(time.strftime("%m.%d %H:%M\t", time.localtime()) + text + "\n" + original_text)




desktop = os.environ.get('COMPUTERNAME')

print("Total 시작   " + time.strftime("%H:%M", time.localtime()))

while True:



    '''
    if time.localtime().tm_wday == 0 and time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:   # 월요일
        print("월요일 주간 던전 오전 7시 30분 작업")

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:   # 아레스 주간 던전
            ares.dungeon_week()   # 아레스 주간 던전
            
    if time.localtime().tm_wday == 1 and time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:   # 화요일
        print("화요일 주간 던전 오전 7시 30분 작업")
        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:   # 아레스 주간 던전
            ares.dungeon_week()   # 아레스 주간 던전
    '''





            
    if time.localtime().tm_wday == 2 and time.localtime().tm_hour == 10 and time.localtime().tm_min == 57:   # 수요일
        print("수요일 점검")
        on.on()



    # 매일 오전 5시 1분    
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 1:
    # if time.localtime().tm_hour == 17 and time.localtime().tm_min == 51:        
        print("오전 5시 뱀피르 작업")

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # 뱀피르 일일던전
            try:
                vp.dungeon(1)
                get_log("오전 5시 뱀피르 작업")
            except Exception as e:
                print(f"vp.dungeon() 오류: " + str(e))


    # 매일 오전 8시 15분    
    if time.localtime().tm_hour == 8 and time.localtime().tm_min == 15:
    # if time.localtime().tm_hour == 19 and time.localtime().tm_min == 55:        
        print("오전 8시 뱀피르 작업")

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # 뱀피르 일일던전
            try:
                vp.dungeon(2)
                get_log("오전 5시 뱀피르 작업")
            except Exception as e:
                print(f"vp.dungeon() 오류: " + str(e))


    # 매일 오전 10시 25분    
    if time.localtime().tm_hour == 10 and time.localtime().tm_min == 25:
    # if time.localtime().tm_hour == 21 and time.localtime().tm_min == 58:        
        print("오전 10시 뱀피르 작업")

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # 뱀피르 일일던전
            try:
                vp.dungeon(3)
                get_log("오전 5시 뱀피르 작업")
            except Exception as e:
                print(f"vp.dungeon() 오류: " + str(e))



                


    # 매일 오전 5시 20분
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 20:
    # if time.localtime().tm_hour == 18 and time.localtime().tm_min == 20:
        
        print("오전 5시 작업")


        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # RF 일일미션
            try:
                rf.dungeon()
                get_log("RF 던전")
            except Exception as e:
                print(f"rf.dungeon() 오류: " + str(e))





    if time.localtime().tm_min in [1, 11, 21, 31, 41, 51]:
        get_log()
    
    # 매시간 1분마다 play    
    if time.localtime().tm_min in [1]:
        print(time.strftime("%H:%M", time.localtime()))

        '''
        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:
            try:
                ares.play()
            except Exception as e:
                print("ares.play() 오류: " + str(e))
        '''

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                rf.play()
            except Exception as e:
                print("rf.play() 오류: " + str(e))
                
            try:
                vp.play()
            except Exception as e:
                print("vp.play() 오류: " + str(e))







        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))
        










    # 매시간 51분마다 a01_start    
    if time.localtime().tm_min in [51]:
        print(time.strftime("%H:%M", time.localtime()))




        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                rf.a01_start()
            except Exception as e:
                print("rf.a01_start() 오류: " + str(e))
                
            try:
                vp.a01_start()
            except Exception as e:
                print("vp.a01_start() 오류: " + str(e))


























    time.sleep(30)
    print(time.strftime("%H:%M", time.localtime()))


print("Total 종료" + " " + time.strftime("%H:%M", time.localtime()))











