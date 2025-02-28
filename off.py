

import jo, lo, ar, dal, ares
import time
import os
import subprocess
import pygetwindow as gw


# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-LRGAL8H"
# "DESKTOP-NT06800"









def off():
    print("off 시작   " + time.strftime("%H:%M", time.localtime()))
    desktop = os.environ.get('COMPUTERNAME')



    for window in gw.getAllWindows(): # 기존의 total.py 닫기
        if 'total' in window.title:
            window.close()

    if 1==1:

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                lo.off()
            except Exception as e:
                print(f"lo.off() 오류: {e}")

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.off()
            except Exception as e:
                print(f"ar.off() 오류: {e}")




        if desktop in ["DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ares.off(0)
            except Exception as e:
                print(f"ares.off() 오류: {e}")
                




        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))

    os.system("shutdown /s /t 0")

if __name__ == "__main__":
    off()






