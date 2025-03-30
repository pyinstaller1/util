

import on, jo, lo, ar, dal, ares, ak
import time
import numpy as np
import keyboard
import os



# "DESKTOP-LRGAL8H"
# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-H9B70U0"
# "DESKTOP-NT06800"



# 달조 매일 오전 5시 dal.play_dal("던전0")
# 달조 매일 오전 7시 dal.play_dal("던전1")

# 아스달 매일 오전 6시 세력 임무 시작 ar.dungeon_ar()
# 아스달 매일 오전 8시 세력 임무 완료 ar.dungeon_ar_end()








# 수요일 점검
# 달조 오후 3시 dal.check_dal()


# 목요일 점검



desktop = os.environ.get('COMPUTERNAME')

print("Total 시작   " + time.strftime("%H:%M", time.localtime()))

while True:
    if time.localtime().tm_wday == 0 and time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:   # 월요일
        print("월요일 주간 던전")
        print("주간 오전 7시 30분 작업")
        ares.dungeon_week_ares()   # 아레스 주간 던전
            
    if time.localtime().tm_wday == 1 and time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:   # 화요일
        print("화요일 주간 던전")
        print("주간 오전 7시 30분 작업")
        ares.dungeon_week_ares()   # 아레스 주간 던전

            
    if time.localtime().tm_wday == 2 and time.localtime().tm_hour == 10 and time.localtime().tm_min == 57:   # 수요일
        print("수요일 점검")
        on.on()



    # 매일 오전 5시 20분
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 20:
        print("오전 5시 작업")
        time.sleep(np.random.randint(30, 180)) # 30초~8분30초 랜덤 대기


        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal("던전0")   # 달빛조각사 불의던전
            except Exception as e:
                print(f"dal.play_dal() 오류: {e}")



        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:   # 아레스 던전
            try:
                ares.dungeon_ares()
            except Exception as e:
                print(f"ar.dungeon_ar() 오류")

                
        # 달조 던전   5시  7시
        # 아레스 던전 5시
        

    # 매일 오전 6시 20분
    if time.localtime().tm_hour == 6 and time.localtime().tm_min == 20:
        print("오전 6시 작업")
        time.sleep(np.random.randint(30, 180)) # 30초~8분30초 랜덤 대기

        # 아스달 던전 6시  8시
        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:    # 아스달 세력임무
            try:
                ar.dungeon_ar()
            except Exception as e:
                try:
                    ar.dungeon_ar()
                except Exception as e:
                    try:
                        ar.dungeon_ar()
                    except Exception as e:
                        try:
                            ar.dungeon_ar()
                        except Exception as e:
                            try:
                                ar.dungeon_ar()
                            except Exception as e:
                                print(f"ar.dungeon_ar() 오류")



                
 


    # 매일 오전 7시 play
    if time.localtime().tm_hour == 7 and time.localtime().tm_min == 20:
        print("오전 7시 작업")
        time.sleep(np.random.randint(30, 511)) # 30초~8분30초 랜덤 대기


        if desktop in ["DESKTOP-OHGK5MV"]:   # 달빛조각사 얼음던전
            try:
                dal.play_dal("던전1")
            except Exception as e:
                print(f"dal.play_dal() 오류")


        # 달조 던전   5시  7시




    # 매일 오전 8시 20분
    if time.localtime().tm_hour == 8 and time.localtime().tm_min == 20:
        print("오전 8시 작업")
        time.sleep(np.random.randint(30, 180)) # 30초~8분30초 랜덤 대기

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:   # 아스달 세력임무 완료
            try:
                ar.dungeon_ar_end()
            except Exception as e:
                try:
                    ar.dungeon_ar_end()
                except Exception as e:
                    try:
                        ar.dungeon_ar_end()
                    except Exception as e:
                        try:
                            ar.dungeon_ar_end()
                        except Exception as e:
                            try:
                                ar.dungeon_ar_end()
                            except Exception as e:
                                print(f"ar.dungeon_ar_end() 오류")







    # 매일 오전 9시 play
    if time.localtime().tm_hour == 9 and time.localtime().tm_min == 20:
        print("오전 9시 작업")
        time.sleep(np.random.randint(30, 511)) # 30초~8분30초 랜덤 대기'

        # 달조 던전   5시  7시
        # 아스달 던전 6시  8시
        # 아레스 던전 5시
        


    # 매시간 1분마다 play    
    if time.localtime().tm_min == 1:
        print(time.strftime("%H:%M", time.localtime()))
        time.sleep(np.random.randint(30, 180)) # 30초~3분 랜덤 대기


        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-LRGAL8H"]:
            try:
                jo.play_lo()
            except Exception as e:
                print(f"jo.play_jo() 오류")

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-LRGAL8H"]:
            try:
                lo.play_lo()
            except Exception as e:
                print(f"lo.play_lo() 오류")

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-H9B70U0"]:
            try:
                ar.play_ar()
            except Exception as e:
                print(f"ar.play_ar() 오류")

        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal()
            except Exception as e:
                print(f"dal.play_dal() 오류")

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                ares.play_ares()
            except Exception as e:
                print(f"ares.play_ares() 오류")
                
        if desktop in ["DESKTOP-H9B70U0"]:
            try:
                ak.play()
            except Exception as e:
                print(f"ak.play() 오류")




        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))
        



    time.sleep(10)
    if keyboard.is_pressed('esc'):  # ESC 키가 눌렸는지 확인
        print("esc")
        break

print("Total 종료" + " " + time.strftime("%H:%M", time.localtime()))











