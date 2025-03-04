import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui
import keyboard





def touch():
    print()
    print(f"Touch {time.strftime('%H:%M', time.localtime())}")


    if time.localtime().tm_min in [38, 47, 57]:
        wins = [win for win in gw.getAllWindows() if 'total' in win.title]
        print(wins)
        win = wins[0]

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

        keyboard.press_and_release('enter')
        time.sleep(3)

        keyboard.press_and_release('enter')

def play_touch():
    while True:
        touch()
        time.sleep(60)

        
        """
        time.sleep(1)
        if keyboard.is_pressed('esc'):  # ESC 키가 눌렸는지 확인
            print("esc")
            break
        """



if __name__ == "__main__":
    play_touch()







