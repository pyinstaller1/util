

import jo, lo, ar
import time
import numpy as np
import keyboard




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
        jo.play_jo()
        lo.play_lo()
        ar.play_ar()
        time.sleep(60)

    time.sleep(1)
    if keyboard.is_pressed('esc'):  # ESC 키가 눌렸는지 확인
        print("esc")
        break

print("Total 종료")



