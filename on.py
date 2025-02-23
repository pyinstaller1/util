

import jo, lo, ar, dal, ares, ymir
import time
import os
import subprocess
import pygetwindow as gw


# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-LRGAL8H"
# "DESKTOP-NT06800"









def on():
    print("on 시작   " + time.strftime("%H:%M", time.localtime()))
    desktop = os.environ.get('COMPUTERNAME')



    for window in gw.getAllWindows(): # 기존의 total.py 닫기
        if 'total' in window.title:
            window.close()

    if 1==1:
        try:
            jo.on()
        except Exception as e:
            print(f"jo.on() 오류: {e}")


        if 1==1 or desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                lo.on()
            except Exception as e:
                print(f"lo.on() 오류: {e}")

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.on()
            except Exception as e:
                print(f"ar.on() 오류: {e}")

        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.on()
            except Exception as e:
                print(f"dal.play_dal() 오류: {e}")


        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                ares.on(0)
            except Exception as e:
                print(f"ar.play_ares() 오류: {e}")
                

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                ymir.on()
            except Exception as e:
                print(f"ymir.play() 오류: {e}")




        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))

    subprocess.Popen(f'start cmd /k python total.py', shell=True)
    os.system("taskkill /F /PID " + str(os.getppid()))


if __name__ == "__main__":
    on()






