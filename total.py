

import jo, lo, ar, dal, ares
import time
import numpy as np
import keyboard
import os


# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-LRGAL8H"
# "DESKTOP-NT06800"



# 달조 매일 오전 5시 dal.play_dal("던전0")
# 달조 매일 오전 7시 dal.play_dal("던전1")

# 아스달 매일 오전 6시 세력 임무 시작 ar.dungeon_ar()
# 아스달 매일 오전 8시 세력 임무 완료 ar.dungeon_ar_end()








# 수요일 점검
# 달조 오후 3시 dal.check_dal()


# 목요일 점검



desktop = os.environ.get('COMPUTERNAME')

while True:


    if time.localtime().tm_wday == 2:   # 월요일
        print("월요일 주간 던전")
        if time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:
            print("주간 오전 7시 30분 작업")
            ares.dungeon_week_ares()

            
    if time.localtime().tm_wday == 2:   # 수요일
        print("수요일 점검")
        if time.localtime().tm_hour == 5 and time.localtime().tm_min == 30:
            print("주간 오전 5시 작업")



    # 매일 오전 5시 10분
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 10:
        print("오전 5시 작업")
        time.sleep(np.random.randint(30, 180)) # 30초~8분30초 랜덤 대기


        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal("던전0")   # 달빛조각사 던전
            except Exception as e:
                print(f"dal.play_dal() 오류: {e}")



        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                ares.dungeon_ares()   # 아레스 던전
            except Exception as e:
                print(f"ar.dungeon_ar() 오류: {e}")

                
        # 달조 던전   5시  7시
        # 아레스 던전 5시
        

    # 매일 오전 6시 10분
    if time.localtime().tm_hour == 6 and time.localtime().tm_min == 10:
        print("오전 6시 작업")
        time.sleep(np.random.randint(30, 180)) # 30초~8분30초 랜덤 대기


        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.dungeon_ar()
            except Exception as e:
                print(f"ar.dungeon_ar() 오류: {e}")
 
        # 아스달 던전 6시  8시


    # 매일 오전 7시 play
    if time.localtime().tm_hour == 7 and time.localtime().tm_min == 10:
        print("오전 7시 작업")
        time.sleep(np.random.randint(30, 511)) # 30초~8분30초 랜덤 대기


        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal("던전1")
            except Exception as e:
                print(f"dal.play_dal() 오류: {e}")


        # 달조 던전   5시  7시




    # 매일 오전 8시 10분
    if time.localtime().tm_hour == 8 and time.localtime().tm_min == 10:
        print("오전 8시 작업")
        time.sleep(np.random.randint(30, 180)) # 30초~8분30초 랜덤 대기

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.dungeon_ar_end()
            except Exception as e:
                print(f"ar.dungeon_ar_end() 오류: {e}")
        
        # 아스달 던전 6시  8시







    # 매일 오전 9시 play
    if time.localtime().tm_hour == 9 and time.localtime().tm_min == 10:
        print("오전 7시 작업")
        time.sleep(np.random.randint(30, 511)) # 30초~8분30초 랜덤 대기'
        # 롬 던전     9시

        # 달조 던전   5시  7시
        # 아스달 던전 6시  8시
        # 아레스 던전 5시
        # 롬 던전     9시
        


    # 매시간 1분마다 play    
    if time.localtime().tm_min == 1:
        print(time.strftime("%H:%M", time.localtime()))
        time.sleep(np.random.randint(30, 180)) # 30초~3분 랜덤 대기


        try:
            jo.play_jo()
        except Exception as e:
            print(f"jo.play_jo() 오류: {e}")


        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                lo.play_lo()
            except Exception as e:
                print(f"lo.play_lo() 오류: {e}")

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.play_ar()
            except Exception as e:
                print(f"ar.play_ar() 오류: {e}")

        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal()
            except Exception as e:
                print(f"dal.play_dal() 오류: {e}")




        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                ares.play_ares()
            except Exception as e:
                print(f"ar.play_ares() 오류: {e}")
                

        print(os.environ.get('COMPUTERNAME'))


    time.sleep(1)
    if keyboard.is_pressed('esc'):  # ESC 키가 눌렸는지 확인
        print("esc")
        break

print("Total 종료")










"""
로드나인 lo2.bok
복구 녹색 계열... ocr 로 확인




"""




