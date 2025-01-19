import time
import pygetwindow as gw
from pywinauto import Application
import pyautogui
import numpy as np
import cv2
import easyocr

# 템플릿 화살표 이미지 로드
img_arrow = cv2.imread('j1.png', cv2.IMREAD_GRAYSCALE)


# 윈도우 목록 가져오기
wins = [win for win in gw.getWindowsWithTitle('LDPlayer') if win.title.strip()]

if not wins:
    print("LDPlayer 윈도우를 찾을 수 없습니다.")

# 윈도우 목록 출력
print("찾은 LDPlayer 윈도우:")
for i, win in enumerate(wins):
    print(f"{i + 1}: {win.title} (위치: {win.left}, {win.top}, 크기: {win.width}x{win.height})")

choice = 0  # 첫 번째 윈도우 선택
win = wins[choice]
print(f"선택된 윈도우: {win.title}")

# pywinauto로 해당 윈도우 활성화
app = Application().connect(handle=win._hWnd)
app.window(handle=win._hWnd).set_focus()

# 윈도우 정보 가져오기
left = win.left
top = win.top
width = win.width
height = win.height
print(f"위치: {left}, {top}")
print(f"크기: {width}x{height}")


# 화면 캡처
screenshot = pyautogui.screenshot(region=(left, top, width, height))
screenshot_np = np.array(screenshot)
screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

result = cv2.matchTemplate(screenshot_gray, img_arrow, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# screenshot1 = pyautogui.screenshot(region=(left+int(width*0.40), top+int(height*0.85), int(width*0.17), height-int(height*0.85)-70))
# screenshot1.save('screen1.png')



scr_check01 = pyautogui.screenshot(region=(left, top+(height-10), 10, 10))
scr_check01_np = np.array(scr_check01)
hsv = cv2.cvtColor(scr_check01_np, cv2.COLOR_RGB2HSV)

# 빨간색 픽셀 탐지
mask = cv2.bitwise_or(
    cv2.inRange(hsv, np.array([0, 50, 50]), np.array([10, 255, 255])),
    cv2.inRange(hsv, np.array([170, 50, 50]), np.array([180, 255, 255]))
)

if not np.any(mask):
    print("빨간색 계열이 발견되었습니다.")
    pyautogui.moveTo(left+(width*0.478), top+(height*0.88), 2.0) # 부활하기

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()

    # time.sleep(300)


    pyautogui.moveTo(left+(width*0.71), top+(height*0.07), 2.0) # 복구

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.17), top+(height*0.9), 2.0) # 복구

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼
        
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.17), top+(height*0.9), 2.0) # 복구

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼
        
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.95), top+(height*0.07), 2.0) # 메뉴

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.95), top+(height*0.18), 2.0) # 사냥도감

    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.055), top+(height*0.46), 2.0) # 요도우라   36  46  56  63  70  78 

    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.17), top+(height*0.33), 2.0) # 맷돼지

    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.91), top+(height*0.95), 2.0) # 이동

    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()






if max_val > 0.8:
    print(777777777)
else:
    print(88888888)



if max_val > 0.8 - 10000:
    print(777777777)

    arrow_x = max_loc[0] + (width*0.025)         # arrow_image.shape[1] // 2
    arrow_y = max_loc[1] + img_arrow.shape[0] // 2


    """
    pyautogui.moveTo(left + arrow_x, top + arrow_y)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(left + arrow_x + (width*0.1), top + arrow_y, 1.0)
    pyautogui.mouseUp()
    """



    """    
    pyautogui.moveTo(left+(width*0.95), top+(height*0.07), 2.0) # 메뉴

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.76), top+(height*0.28), 2.0) # 장비도감

    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.83), top+(height*0.93), 2.0) # 장비도감 일괄등록
        
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.57), top+(height*0.65), 2.0) # 확인 버튼
        
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()

    time.sleep(3.0)

    
    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.96), top+(height*0.08), 2.0) # 장비도감 종료

    pyautogui.mouseDown()
    time.sleep(0.3)
    pyautogui.mouseUp()



    """



















    """
    pyautogui.moveTo(left+(width*0.95), top+(height*0.07), 2.0) # 메뉴

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




    pyautogui.moveTo(left+(width*0.81), top+(height*0.08), 2.0) # 가방

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()




    pyautogui.moveTo(left+(width*0.81), top+(height*0.925), 2.0) # 분해

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.417), top+(height*0.638), 2.0) # 장비

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.417), top+(height*0.68), 2.0) # 일반

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()


    pyautogui.moveTo(left+(width*0.47), top+(height*0.68), 2.0) # 고급

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.57), top+(height*0.81), 2.0) # 분해버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    


    pyautogui.moveTo(left+(width*0.56), top+(height*0.638), 2.0) # 확인버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    

    pyautogui.moveTo(left+(width*0.5), top+(height*0.638), 2.0) # 확인버튼

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()



    pyautogui.moveTo(left+(width*0.05), top+(height*0.73), 2.0) # 절전

    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    """



    



    

"""

arrow_x = max_loc[0] + (width*0.025)         # arrow_image.shape[1] // 2
arrow_y = max_loc[1] + img_arrow.shape[0] // 2

pyautogui.moveTo(left + arrow_x, top + arrow_y)

# OCR 처리 시간 측정 시작
start_time = time.time()

# OCR 객체 생성 및 텍스트 추출
reader = easyocr.Reader(['ko', 'en'], gpu=False)
results = reader.readtext(screenshot_np)

# OCR 처리 시간 측정 끝
end_time = time.time()

# 소요 시간 출력
elapsed_time = end_time - start_time
print(f"OCR 처리에 걸린 시간: {elapsed_time:.2f} 초")

# 텍스트와 중심 좌표 출력
print("OCR 텍스트 및 좌표:")
for detection in results:
    bbox, text, confidence = detection
    top_left = bbox[0]
    bottom_right = bbox[2]
    x = (top_left[0] + bottom_right[0]) // 2
    y = (top_left[1] + bottom_right[1]) // 2
    print(f"{text} [{x}, {y}]")
"""





