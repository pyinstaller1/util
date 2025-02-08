

import jo, lo, ar
import time
import numpy as np
import keyboard
import os


# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-LRGAL8H"
# "DESKTOP-NT06800"

desktop = os.environ.get('COMPUTERNAME')

while True:

    # 매일 오전 7시 play
    if time.localtime().tm_hour == 7 and time.localtime().tm_min == 1:
        print("오전 작업")
        time.sleep(np.random.randint(30, 511)) # 30초~8분30초 랜덤 대기
        # 아스달 던전
        # 아레스 던전
        # 달조 던전
        # 롬 던전
        


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
                print(f"ar.play_ar() 오류: {e}")

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




