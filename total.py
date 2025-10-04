

import on, jo, lo, ar, dal, ares, ak, rf, vp, odin
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



# 달조 매일 오전 5시 dal.play_dal("던전0")
# 달조 매일 오전 7시 dal.play_dal("던전1")

# 아레스 매일 오전 5시 dal.play_dal("던전0")

# 아스달 매일 오전 6시 세력 임무 시작 ar.dungeon_ar()
# 아스달 매일 오전 8시 세력 임무 완료 ar.dungeon_ar_end()




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
    if time.localtime().tm_wday == 0 and time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:   # 월요일
        print("월요일 주간 던전 오전 7시 30분 작업")

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:   # 아레스 주간 던전
            ares.dungeon_week()   # 아레스 주간 던전
            
    if time.localtime().tm_wday == 1 and time.localtime().tm_hour == 7 and time.localtime().tm_min == 30:   # 화요일
        print("화요일 주간 던전 오전 7시 30분 작업")
        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:   # 아레스 주간 던전
            ares.dungeon_week()   # 아레스 주간 던전





            
    if time.localtime().tm_wday == 2 and time.localtime().tm_hour == 10 and time.localtime().tm_min == 57:   # 수요일
        print("수요일 점검")
        on.on()




    # 매일 오전 4시 1분    
    if time.localtime().tm_hour == 4 and time.localtime().tm_min == 1:
        print("오전 4시 오딘 1번 던전")

        if desktop in ["DESKTOP-H9B70U0"]:   # 오딘 일일던전
            try:
                odin.dungeon(1, 2)   # 1번 캐릭터 2번 던전
            except Exception as e:
                print(f"odin.dungeon() 오류: " + str(e))


    # 매일 오전 5시 30분    
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 31:
        print("오전 5시 오딘 2번 던전")

        if desktop in ["DESKTOP-H9B70U0"]:   # 오딘 일일던전
            try:
                odin.dungeon(2, 2)   # 2번 캐릭터 2번 던전
            except Exception as e:
                print(f"odin.dungeon() 오류: " + str(e))


    # 매일 오전 7시 1분    
    if time.localtime().tm_hour == 7 and time.localtime().tm_min == 1:
        print("오전 7시 오딘 3번 던전")

        if desktop in ["DESKTOP-H9B70U0"]:   # 오딘 일일던전
            try:
                odin.dungeon(3, 2)   # 3번 캐릭터 2번 던전
            except Exception as e:
                print(f"odin.dungeon() 오류: " + str(e))



    # 매일 오전 8시 31분    
    if time.localtime().tm_hour == 8 and time.localtime().tm_min == 31:
        print("오전 8시 오딘 4번 던전")

        if desktop in ["DESKTOP-H9B70U0"]:   # 오딘 일일던전
            try:
                odin.dungeon(4, 2)   # 3번 캐릭터 2번 던전
            except Exception as e:
                print(f"odin.dungeon() 오류: " + str(e))

    # 매일 오전 10시 1분    
    if time.localtime().tm_hour == 10 and time.localtime().tm_min == 1:
        print("오전 10시 오딘 5번 던전")

        if desktop in ["DESKTOP-H9B70U0"]:   # 오딘 일일던전
            try:
                odin.dungeon(5, 2)   # 3번 캐릭터 2번 던전
            except Exception as e:
                print(f"odin.dungeon() 오류: " + str(e))


    # 매일 오전 11시 31분    
    if time.localtime().tm_hour == 10 and time.localtime().tm_min == 1:
        print("오전 11시 오딘 주간 던전")

        if desktop in ["DESKTOP-H9B70U0"]:   # 오딘 일일던전
            try:
                odin.dungeon((((datetime.date.today().weekday()) % 5) + 1), 3)   # 요일마다 3번 던전
            except Exception as e:
                print(f"odin.dungeon() 오류: " + str(e))













    # 매일 오전 5시 1분    
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 1:
        print("오전 5시 뱀피르 작업")

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # 뱀피르 일일던전
            try:
                vp.dungeon(1)
                get_log("오전 5시 뱀피르 작업")
            except Exception as e:
                print(f"ares.dungeon() 오류: " + str(e))


    # 매일 오전 8시 15분    
    if time.localtime().tm_hour == 8 and time.localtime().tm_min == 15:
        print("오전 8시 뱀피르 작업")

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # 뱀피르 일일던전
            try:
                vp.dungeon(2)
                get_log("오전 5시 뱀피르 작업")
            except Exception as e:
                print(f"ares.dungeon() 오류: " + str(e))


    # 매일 오전 10시 25분    
    if time.localtime().tm_hour == 10 and time.localtime().tm_min == 25:
        print("오전 10시 뱀피르 작업")

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # 뱀피르 일일던전
            try:
                vp.dungeon(3)
                get_log("오전 5시 뱀피르 작업")
            except Exception as e:
                print(f"ares.dungeon() 오류: " + str(e))



                


    # 매일 오전 5시 20분
    if time.localtime().tm_hour == 5 and time.localtime().tm_min == 20:
        print("오전 5시 작업")

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:   # 아레스 일일던전
            try:
                ares.dungeon()
                get_log("아레스 던전")
            except Exception as e:
                print(f"ares.dungeon() 오류: " + str(e))

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:   # RF 일일미션
            try:
                rf.dungeon()
                get_log("RF 던전")
            except Exception as e:
                print(f"rf.dungeon() 오류: " + str(e))


        
        '''
        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal("던전0")   # 달빛조각사 불의던전
            except Exception as e:
                print(f"dal.play_dal() 오류: {e}")
        '''


        

    '''
    # 매일 오전 6시 20분
    if time.localtime().tm_hour == 6 and time.localtime().tm_min == 20:
        print("오전 6시 작업")

        # 아스달 던전 6시  8시
        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-H9B70U0"]:    # 아스달 세력임무
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
                                print(f"ar.dungeon_ar() 오류: " + str(e))
                
    '''

    '''
    # 매일 오전 7시 play
    if time.localtime().tm_hour == 7 and time.localtime().tm_min == 20:
        print("오전 7시 작업")
        time.sleep(np.random.randint(30, 511)) # 30초~8분30초 랜덤 대기


        if desktop in ["DESKTOP-OHGK5MV"]:   # 달빛조각사 얼음던전
            try:
                dal.play_dal("던전1")
            except Exception as e:
                print(f"dal.play_dal() 오류: " + str(e))


        # 달조 던전   5시  7시

    '''





    '''
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
                                print(f"ar.dungeon_ar_end() 오류: " + str(e))

    '''


    if time.localtime().tm_min in [1, 11, 21, 31, 41, 51]:
        get_log()
    
    # 매시간 1분마다 play    
    if time.localtime().tm_min in [1]:
        print(time.strftime("%H:%M", time.localtime()))

        '''
        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                jo.play()
            except Exception as e:
                print("jo.play() 오류: " + str(e))


        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                lo.play()
            except Exception as e:
                print("lo.play() 오류: " + str(e))
        '''

        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:
            try:
                ares.play()
            except Exception as e:
                print("ares.play() 오류: " + str(e))

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                rf.play()
            except Exception as e:
                print("rf.play() 오류: " + str(e))
                
            try:
                vp.play()
            except Exception as e:
                print("vp.play() 오류: " + str(e))

        if desktop in ["DESKTOP-H9B70U0"]:
            try:
                odin.play()
            except Exception as e:
                print("odin.play() 오류: " + str(e))
                

        '''
        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-H9B70U0"]:
            try:
                ar.play_ar()
            except Exception as e:
                print("ar.play_ar() 오류: " + str(e))

        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.play_dal()
            except Exception as e:
                print(f"dal.play_dal() 오류: " + str(e))
     
        if desktop in ["DESKTOP-H9B70U0"]:
            try:
                ak.play()
            except Exception as e:
                print("ak.play() 오류: " + str(e))
        '''





        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))
        



    time.sleep(30)
    print(time.strftime("%H:%M", time.localtime()))


print("Total 종료" + " " + time.strftime("%H:%M", time.localtime()))











