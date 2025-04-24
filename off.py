

import jo, lo, ar, dal, ares, rf, dk
import time
import os
import subprocess
import pygetwindow as gw


# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-LRGAL8H"
# "DESKTOP-H9B70U0"
# "DESKTOP-NT06800"









def off():
    print("off 시작   " + time.strftime("%H:%M", time.localtime()))
    desktop = os.environ.get('COMPUTERNAME')



    for window in gw.getAllWindows(): # 기존의 total.py 닫기
        if 'total' in window.title:
            window.close()

    if 1==1:

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H", "DESKTOP-H9B70U0"]:
            try:
                lo.off()
            except Exception as e:
                print(f"lo.off() 오류")

        '''
        if desktop in ["DESKTOP-H9B70U0", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB"]:
            try:
                ar.off()
            except Exception as e:
                print(f"ar.off() 오류")
        '''




        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-H9B70U0"]:
            try:
                ares.off()
            except Exception as e:
                print(f"ares.off() 오류")
                


        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0"]:
            try:
                rf.off()
            except Exception as e:
                print(f"rf.off() 오류")
                

        if desktop in ["DESKTOP-LRGAL8H", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-OHGK5MV", "DESKTOP-H9B70U0", "DESKTOP-NT06800"]:
            try:
                dk.off()
            except Exception as e:
                print(f"dk.off() 오류")
                

        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))

    os.system("shutdown /s /t 0")

if __name__ == "__main__":
    off()






