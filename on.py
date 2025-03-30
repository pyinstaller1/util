

import jo, lo, ar, dal, ares, ak
import time
import os
import subprocess
import pygetwindow as gw


# "DESKTOP-LRGAL8H"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-OHGK5MV"
# "DESKTOP-H9B70U0"
# "DESKTOP-NT06800"








def on():
    print("on 시작   " + time.strftime("%H:%M", time.localtime()))
    desktop = os.environ.get('COMPUTERNAME')



    for window in gw.getAllWindows(): # 기존의 total.py 닫기
        if 'total' in window.title:
            window.close()

    if 1==1:

        time.sleep(600)

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                jo.on()
            except Exception as e:
                print(f"jo.on() 오류")
            

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                lo.on()
            except Exception as e:
                print(f"lo.on() 오류")


        if desktop in ["DESKTOP-H9B70U0", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.on()
            except Exception as e:
                print(f"ar.on() 오류")

        if desktop in ["DESKTOP-OHGK5MV"]:
            try:
                dal.on()
            except Exception as e:
                print(f"dal.on() 오류")


        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                ares.on(0)
            except Exception as e:
                print(f"ares.on() 오류")
            

        if desktop in ["DESKTOP-H9B70U0"]:
            try:
                ak.on()
            except Exception as e:
                print(f"ak.on() 오류")





        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))

    subprocess.Popen(f'start cmd /k python total.py', shell=True)
    os.system("taskkill /F /PID " + str(os.getppid()))


if __name__ == "__main__":
    on()






