import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui
import numpy as np
import cv2
import easyocr
import re
import psutil
import subprocess
import sys





# os.system(f"taskkill /F /IM {process_name}")

if len(sys.argv) > 1:
    target_name = sys.argv[1].lower()
else:
    target_name = ""


    
for proc in psutil.process_iter():
    print(proc.name())
    continue

    if target_name in proc.name().lower():
            print(proc.name())



"""
for proc in psutil.process_iter():
    if proc.name().lower() == "stove.exe":
        proc.kill()
        print(f"{proc.name()} 종료됨")
"""



"""

def 01a():
    print(7)
01a()
"""


'''
wins = gw.getAllWindows()
for win in wins:
    print(win)
'''

"""
for window in gw.getAllWindows():
    if 'total' in window.title:
        window.close()
"""

        


"""
import time

def get_weekday():
    days = ["월", "화", "수", "목요일", "금요일", "토요일", "일요일"]
    return days[time.localtime().tm_wday]  # tm_wday는 0(월요일) ~ 6(일요일) 값을 가짐

# 실행 예제
print(f"오늘은 {time.localtime().tm_wday}입니다.")
"""








"""
pyautogui.moveTo(800, 800, 2.0)
pyautogui.mouseDown()
time.sleep(1)
pyautogui.moveTo(1000, 800, 2.0)
pyautogui.mouseUp()
"""









"""
scr_google = pyautogui.screenshot(region=(880, 380, 380, 500))

scr_google_np = np.array(scr_google)
scr_google.save("scr_dal_google.png")

# 복구 ocr 탐지
reader = easyocr.Reader(['ko', 'en'], gpu=False)
results = reader.readtext(scr_google_np)
print(results)
"""








"""
import time
import pyautogui
import tkinter as tk
from tkinter import ttk

def move_mouse():
    status_label.config(text="작업 진행 중...", fg="red")
    root.update()

    total_steps = 20  # 전체 진행 단계를 20으로 설정 (10단계씩 2회 이동)
    
    for i in range(2):  # 2번 이동
        x, y = 500 + (i * 100), 500 + (i * 50)  # 이동 좌표 변경

        for j in range(10):  # 각 이동을 10단계로 나누어 진행 바 업데이트
            progress["value"] += (100 / total_steps)
            root.update()
            pyautogui.moveTo(x, y, duration=0.1)  # 마우스 천천히 이동
            time.sleep(0.1)

        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()

    status_label.config(text="완료!", fg="green")
    progress["value"] = 100
    root.update()

    time.sleep(1)  # 완료 메시지 표시 후 대기
    root.destroy()  # 창 닫기

# Tkinter 창 설정
root = tk.Tk()
root.attributes("-topmost", True)  # 항상 위에 표시
root.overrideredirect(True)  # 창 테두리 없애기
root.geometry("250x80+600+300")  # 화면 중앙 배치

# 진행 상태 라벨
status_label = tk.Label(root, text="준비 중...", font=("Arial", 14), bg="white")
status_label.pack()

# 진행 바 추가
progress = ttk.Progressbar(root, length=200, mode="determinate")
progress.pack(pady=10)

# 실행 즉시 마우스 이동 시작
root.after(500, move_mouse)  # 0.5초 후 실행 (UI 표시 후 실행)

root.mainloop()
"""













"""

import tkinter as tk
import random

# 파스텔톤 색상 변경 애니메이션 (천천히 색 변하기)
def change_background_color(root, label, current_color):
    # 파스텔톤 색상 범위 (밝고 부드러운 색상들)
    r = (current_color[0] + random.randint(1, 3)) % 256  # 빨강 (1~3만큼만 변화)
    g = (current_color[1] + random.randint(1, 3)) % 256  # 초록 (1~3만큼만 변화)
    b = (current_color[2] + random.randint(1, 3)) % 256  # 파랑 (1~3만큼만 변화)

    # 파스텔톤 색상 범위 (밝은 색들만)
    r = min(255, max(200, r))  # 빨강 값은 200~255 사이
    g = min(255, max(200, g))  # 초록 값은 200~255 사이
    b = min(255, max(200, b))  # 파랑 값은 200~255 사이

    # 전체 배경 색상 적용
    root.configure(bg=f"#{r:02x}{g:02x}{b:02x}")
    
    # 텍스트 배경 색상 변경
    label.config(bg=f"#{r:02x}{g:02x}{b:02x}")

    # 계속해서 배경 색상이 변하도록 100ms마다 호출 (좀 더 천천히 변)
    root.after(100, change_background_color, root, label, (r, g, b))

# 작업중 텍스트 표시
def create_working_window():
    root = tk.Tk()
    root.title("작업중")
    
    # 윈도우 크기 설정
    width = 500
    height = 200
    root.geometry(f"{width}x{height}+{500}+{300}")  # 화면 가운데 위치

    # 창 설정
    root.overrideredirect(True)  # 창 테두리 제거
    root.attributes("-topmost", True)  # 항상 위에 표시

    # 초기 색상 설정 (파스텔톤)
    initial_color = (200, 200, 200)  # 처음 색상 (회색 계열)

    # "작업중" 텍스트 표시 (글자 크기와 굵기 증가)
    label = tk.Label(root, text="작업중", fg="blue", font=("Arial", 48, "bold"), bg="#ffffff")
    label.place(x=width//4, y=height//3)  # 텍스트 위치 설정

    # 색상 변경 애니메이션 시작
    change_background_color(root, label, initial_color)

    # Tkinter 이벤트 루프 실행
    root.mainloop()

# 실행
create_working_window()
"""









print(7)
