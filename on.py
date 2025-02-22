

import jo, lo, ar, dal, ares, ymir
import time
import numpy as np
import keyboard
import os


# "DESKTOP-OHGK5MV"
# "DESKTOP-MA2NLC4"
# "DESKTOP-792RKKB"
# "DESKTOP-LRGAL8H"
# "DESKTOP-NT06800"









def on():
    print("on 시작   " + time.strftime("%H:%M", time.localtime()))
    desktop = os.environ.get('COMPUTERNAME')

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
                ares.on()
            except Exception as e:
                print(f"ar.play_ares() 오류: {e}")
                

        if desktop in ["DESKTOP-OHGK5MV", "DESKTOP-MA2NLC4", "DESKTOP-792RKKB", "DESKTOP-LRGAL8H"]:
            try:
                ymir.on()
            except Exception as e:
                print(f"ymir.play() 오류: {e}")




        print(os.environ.get('COMPUTERNAME') + " " + time.strftime("%H:%M", time.localtime()))





if __name__ == "__main__":
    on()






