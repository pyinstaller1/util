import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui






def touch():
    print()
    print(f"Touch {time.strftime('%H:%M', time.localtime())}")


    wins = [win for win in gw.getAllWindows() if 'cmd' in win.title]
    win = wins[1]

    app = Application().connect(handle=win._hWnd)
    app.window(handle=win._hWnd).set_focus()


    global left, top, width, height
    left = win.left
    top = win.top
    width = win.width
    height = win.height



    pyautogui.click(left+(width*0.5), top+(height*0.5))


    time.sleep(3)


    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.press('enter')

def play_touch():
    while True:
        touch()
        time.sleep(600)
    





if __name__ == "__main__":
    # touch()
    play_touch()







