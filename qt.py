from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class Robot(QWidget):
    def __init__(self):
        super().__init__()

        # "연계점검 로봇" 라벨 추가
        self.label_robot_title = QLabel('연계점검 로봇 🤖', self)
        self.label_robot_title.setStyleSheet("font-size: 33px; font-weight: bold;")




        self.group_a123 = QGroupBox("건강 ERP", self)
        self.group_a123.setGeometry(15, 70, 220, 225)
        self.group_a123.setStyleSheet("font-size: 12px; font-weight: bold;")

        self.group_a3 = QGroupBox("", self)
        self.group_a3.setGeometry(20, 145, 210, 143)


        self.group_a456 = QGroupBox("징수통합", self)
        self.group_a456.setGeometry(15, 310, 220, 198)
        self.group_a456.setStyleSheet("font-size: 12px; font-weight: bold;")

        self.group_a6 = QGroupBox("", self)
        self.group_a6.setGeometry(20, 385, 210, 116)


        self.group_a789 = QGroupBox("장기요양", self)
        self.group_a789.setGeometry(15, 523, 220, 225)
        self.group_a789.setStyleSheet("font-size: 12px; font-weight: bold;")

        self.group_a9 = QGroupBox("", self)
        self.group_a9.setGeometry(20, 598, 210, 143)



        

        # 라벨 생성
        self.label_result_title = QLabel('점검결과', self)  # 점검결과 라벨
        self.label_result_title.setStyleSheet("font-weight: bold;")        
        self.label_input_title = QLabel('정상기준', self)  # 정상기준 라벨
        self.label_input_title.setStyleSheet("font-weight: bold;")
        
        self.label01 = QLabel('처리중', self)
        self.label02 = QLabel('오류', self)
        self.label03_1 = QLabel('AGENT', self)
        self.label03_2 = QLabel('RUNNER', self)
        self.label03_3 = QLabel('채널', self)
        self.label03_4 = QLabel('큐깊이', self)
        self.label03_5 = QLabel('IIP AGENT', self)

        self.label04 = QLabel('처리중', self)
        self.label05 = QLabel('오류', self)
        self.label06_1 = QLabel('AGENT', self)
        self.label06_2 = QLabel('RUNNER', self)
        self.label06_3 = QLabel('채널', self)
        self.label06_4 = QLabel('IIP AGENT', self)

        self.label07 = QLabel('처리중', self)
        self.label08 = QLabel('오류', self)
        self.label09_1 = QLabel('AGENT', self)
        self.label09_2 = QLabel('RUNNER', self)
        self.label09_3 = QLabel('채널', self)
        self.label09_4 = QLabel('큐깊이', self)
        self.label09_5 = QLabel('IIP AGENT', self)
        
        self.label10 = QLabel('오류', self)




        # 인풋 생성
        self.edit_input01 = QLineEdit(self)
        self.edit_input02 = QLineEdit(self)
        self.edit_input03_1 = QLineEdit(self)
        self.edit_input03_2 = QLineEdit(self)
        self.edit_input03_3 = QLineEdit(self)
        self.edit_input03_4 = QLineEdit(self)
        self.edit_input03_5 = QLineEdit(self)

        self.edit_input04 = QLineEdit(self)
        self.edit_input05 = QLineEdit(self)
        self.edit_input06_1 = QLineEdit(self)
        self.edit_input06_2 = QLineEdit(self)
        self.edit_input06_3 = QLineEdit(self)
        self.edit_input06_4 = QLineEdit(self)

        self.edit_input07 = QLineEdit(self)
        self.edit_input08 = QLineEdit(self)
        self.edit_input09_1 = QLineEdit(self)
        self.edit_input09_2 = QLineEdit(self)
        self.edit_input09_3 = QLineEdit(self)
        self.edit_input09_4 = QLineEdit(self)
        self.edit_input09_5 = QLineEdit(self)

        self.edit_input10 = QLineEdit(self)


        

        # 결과 인풋 생성
        self.edit_result01 = QLineEdit(self)
        self.edit_result02 = QLineEdit(self)
        self.edit_result03_1 = QLineEdit(self)
        self.edit_result03_2 = QLineEdit(self)
        self.edit_result03_3 = QLineEdit(self)
        self.edit_result03_4 = QLineEdit(self)
        self.edit_result03_5 = QLineEdit(self)

        self.edit_result04 = QLineEdit(self)
        self.edit_result05 = QLineEdit(self)
        self.edit_result06_1 = QLineEdit(self)
        self.edit_result06_2 = QLineEdit(self)
        self.edit_result06_3 = QLineEdit(self)
        self.edit_result06_4 = QLineEdit(self)

        self.edit_result07 = QLineEdit(self)
        self.edit_result08 = QLineEdit(self)
        self.edit_result09_1 = QLineEdit(self)
        self.edit_result09_2 = QLineEdit(self)
        self.edit_result09_3 = QLineEdit(self)
        self.edit_result09_4 = QLineEdit(self)
        self.edit_result09_5 = QLineEdit(self)

        self.edit_result10 = QLineEdit(self)





        
        
        self.edit_result01.setReadOnly(True)
        self.edit_result02.setReadOnly(True)
        self.edit_result03_1.setReadOnly(True)
        self.edit_result03_2.setReadOnly(True)
        self.edit_result03_3.setReadOnly(True)
        self.edit_result03_4.setReadOnly(True)
        self.edit_result03_5.setReadOnly(True)
        
        self.edit_result04.setReadOnly(True)
        self.edit_result05.setReadOnly(True)
        self.edit_result06_1.setReadOnly(True)
        self.edit_result06_2.setReadOnly(True)
        self.edit_result06_3.setReadOnly(True)
        self.edit_result06_4.setReadOnly(True)

        self.edit_result07.setReadOnly(True)
        self.edit_result08.setReadOnly(True)
        self.edit_result09_1.setReadOnly(True)
        self.edit_result09_2.setReadOnly(True)
        self.edit_result09_3.setReadOnly(True)
        self.edit_result09_4.setReadOnly(True)
        self.edit_result09_5.setReadOnly(True)        

        self.edit_result10.setReadOnly(True)


        

        # self.edit_result01.setStyleSheet("background-color: #FFFF00; border: 1px solid gray;")  # 셀 내부 배경색을 노란색으로 설정

        
        self.lb_g_01 = QLabel('건', self)
        self.lb_g_02 = QLabel('건', self)
        self.lb_g_03_1 = QLabel('건', self)
        self.lb_g_03_2 = QLabel('건', self)
        self.lb_g_03_3 = QLabel('건', self)
        self.lb_g_03_4 = QLabel('건', self)
        self.lb_g_03_5 = QLabel('건', self)

        self.lb_g_04 = QLabel('건', self)
        self.lb_g_05 = QLabel('건', self)
        self.lb_g_06_1 = QLabel('건', self)
        self.lb_g_06_2 = QLabel('건', self)
        self.lb_g_06_3 = QLabel('건', self)
        self.lb_g_06_4 = QLabel('건', self)
        self.lb_g_06_5 = QLabel('건', self)

        self.lb_g_07 = QLabel('건', self)
        self.lb_g_08 = QLabel('건', self)
        self.lb_g_09_1 = QLabel('건', self)
        self.lb_g_09_2 = QLabel('건', self)
        self.lb_g_09_3 = QLabel('건', self)
        self.lb_g_09_4 = QLabel('건', self)
        self.lb_g_09_5 = QLabel('건', self)

        self.lb_g_10 = QLabel('건', self)


        

        self.lb_result_01 = QLabel('정상', self)
        self.lb_result_02 = QLabel('정상', self)
        self.lb_result_03 = QLabel('정상', self)

        self.lb_result_04 = QLabel('정상', self)
        self.lb_result_05 = QLabel('정상', self)
        self.lb_result_06 = QLabel('정상', self)

        self.lb_result_07 = QLabel('정상', self)
        self.lb_result_08 = QLabel('정상', self)
        self.lb_result_09 = QLabel('정상', self)

        self.lb_result_10 = QLabel('정상', self)        


        # 인풋 설정
        for edit_field in [self.edit_input01, self.edit_input02, self.edit_input03_1, self.edit_input03_2, self.edit_input03_3, self.edit_input03_4, self.edit_input03_5,
                           self.edit_input04, self.edit_input05, self.edit_input06_1, self.edit_input06_2, self.edit_input06_3, self.edit_input06_4,
                           self.edit_input07, self.edit_input08, self.edit_input09_1, self.edit_input09_2, self.edit_input09_3, self.edit_input09_4, self.edit_input09_5, self.edit_input10]:
            edit_field.setFixedWidth(50)  # 너비 고정
            edit_field.setFixedHeight(25)  # 높이 고정
            edit_field.setAlignment(Qt.AlignRight)  # 오른쪽 정렬
            edit_field.setStyleSheet("font-size: 16px;")  # 글자 크기 16px로 설정
            edit_field.textChanged.connect(self.add_comma)

        # 결과 인풋 설정
        for edit_field in [self.edit_result01, self.edit_result02, self.edit_result03_1, self.edit_result03_2, self.edit_result03_3, self.edit_result03_4, self.edit_result03_5,
                           self.edit_result04, self.edit_result05, self.edit_result06_1, self.edit_result06_2, self.edit_result06_3, self.edit_result06_4,
                           self.edit_result07, self.edit_result08, self.edit_result09_1, self.edit_result09_2, self.edit_result09_3, self.edit_result09_4, self.edit_result09_5, self.edit_result10]:
            edit_field.setFixedWidth(50)  # 너비 고정
            edit_field.setFixedHeight(25)  # 높이 고정
            edit_field.setAlignment(Qt.AlignRight)  # 오른쪽 정렬
            edit_field.setStyleSheet("font-size: 16px;")  # 글자 크기 16px로 설정
            edit_field.textChanged.connect(self.add_comma)

        # 슬래시 라벨
        self.slash_label01 = QLabel('/', self)
        self.slash_label02 = QLabel('/', self)
        self.slash_label03_1 = QLabel('/', self)
        self.slash_label03_2 = QLabel('/', self)
        self.slash_label03_3 = QLabel('/', self)
        self.slash_label03_4 = QLabel('/', self)
        self.slash_label03_5 = QLabel('/', self)

        self.slash_label04 = QLabel('/', self)
        self.slash_label05 = QLabel('/', self)
        self.slash_label06_1 = QLabel('/', self)
        self.slash_label06_2 = QLabel('/', self)
        self.slash_label06_3 = QLabel('/', self)
        self.slash_label06_4 = QLabel('/', self)

        self.slash_label07 = QLabel('/', self)
        self.slash_label08 = QLabel('/', self)
        self.slash_label09_1 = QLabel('/', self)
        self.slash_label09_2 = QLabel('/', self)
        self.slash_label09_3 = QLabel('/', self)
        self.slash_label09_4 = QLabel('/', self)
        self.slash_label09_5 = QLabel('/', self)
        
        self.slash_label10 = QLabel('/', self)



        # 슬래시 라벨 크기 23px로 설정
        self.slash_label01.setStyleSheet("font-size: 23px;")
        self.slash_label02.setStyleSheet("font-size: 23px;")
        self.slash_label03_1.setStyleSheet("font-size: 23px;")
        self.slash_label03_2.setStyleSheet("font-size: 23px;")
        self.slash_label03_3.setStyleSheet("font-size: 23px;")
        self.slash_label03_4.setStyleSheet("font-size: 23px;")
        self.slash_label03_5.setStyleSheet("font-size: 23px;")

        self.slash_label04.setStyleSheet("font-size: 23px;")
        self.slash_label05.setStyleSheet("font-size: 23px;")
        self.slash_label06_1.setStyleSheet("font-size: 23px;")
        self.slash_label06_2.setStyleSheet("font-size: 23px;")
        self.slash_label06_3.setStyleSheet("font-size: 23px;")
        self.slash_label06_4.setStyleSheet("font-size: 23px;")

        self.slash_label07.setStyleSheet("font-size: 23px;")
        self.slash_label08.setStyleSheet("font-size: 23px;")
        self.slash_label09_1.setStyleSheet("font-size: 23px;")
        self.slash_label09_2.setStyleSheet("font-size: 23px;")
        self.slash_label09_3.setStyleSheet("font-size: 23px;")
        self.slash_label09_4.setStyleSheet("font-size: 23px;")
        self.slash_label09_5.setStyleSheet("font-size: 23px;")

        self.slash_label10.setStyleSheet("font-size: 23px;")






        # 레이아웃 설정
        self.setGeometry(200, 100, 500, 880)
        self.setWindowTitle('연계점검 로봇 🤖')  # 타이틀바에 로봇 이모지 추가

        # 위치 설정
        self.label_robot_title.move(10, 3)  # "연계점검 로봇" 라벨 위치

        self.label_result_title.move(90, 55)  # 점검결과 라벨
        self.label_input_title.move(161, 55)  # 정상기준 라벨






        # 건강ERP
        # 01 점검중
        self.label01.move(50, 97)
        self.edit_result01.move(90, 90)
        self.slash_label01.move(145, 90)
        self.edit_input01.move(160, 90)
        self.lb_g_01.move(215, 97)
        self.lb_result_01.move(243, 97)
        

        # 02 오류
        self.label02.move(62, 124)
        self.edit_result02.move(90, 117)
        self.slash_label02.move(145, 117)
        self.edit_input02.move(160, 117)
        self.lb_g_02.move(215, 124)
        self.lb_result_02.move(243, 124)


        # 03_1 AGENT
        self.label03_1.move(43, 156)  # 117 + 25 + 10 = 149
        self.edit_result03_1.move(90, 149)
        self.slash_label03_1.move(145, 149)
        self.edit_input03_1.move(160, 149)
        self.lb_g_03_1.move(215, 156)

        # 03_2 RUNNER
        self.label03_2.move(37, 183)  # 149 + 25 + 2 = 176
        self.edit_result03_2.move(90, 176)
        self.slash_label03_2.move(145, 176)
        self.edit_input03_2.move(160, 176)
        self.lb_g_03_2.move(215, 183)
        

        # 03_3 채널
        self.label03_3.move(62, 210)  # 176 + 25 + 2 = 203
        self.edit_result03_3.move(90, 203)
        self.slash_label03_3.move(145, 203)
        self.edit_input03_3.move(160, 203)
        self.lb_g_03_3.move(215, 210)
        self.lb_result_03.move(243, 210)

        '''
        self.lb_result_03.setText('이상')  # 내용 변경
        self.lb_result_03.setStyleSheet("font-size: 15px; color: blue; font-weight: bold;")  # 파란색, 굵게 설정
        self.lb_result_03.move(243, 209)        
        '''

        # 03_4 큐깊이
        self.label03_4.move(50, 237)  # 203 + 25 + 2 = 230
        self.edit_result03_4.move(90, 230)
        self.slash_label03_4.move(145, 230)
        self.edit_input03_4.move(160, 230)
        self.lb_g_03_4.move(215, 237)
        

        # 03_5 IIP AGENT
        self.label03_5.move(25, 264)  # 230 + 25 + 2 = 257
        self.edit_result03_5.move(90, 257)
        self.slash_label03_5.move(145, 257)
        self.edit_input03_5.move(160, 257)
        self.lb_g_03_5.move(215, 264)







        # 징수통합
        # 04 점검중
        self.label04.move(50, 337)       # 징수통합 점검중
        self.edit_result04.move(90, 330)
        self.slash_label04.move(145, 330)
        self.edit_input04.move(160, 330)
        self.lb_g_04.move(215, 337)
        self.lb_result_04.move(243, 337)

        # 05 오류
        self.label05.move(62, 364)
        self.edit_result05.move(90, 357)
        self.slash_label05.move(145, 357)
        self.edit_input05.move(160, 357)
        self.lb_g_05.move(215, 364)
        self.lb_result_05.move(243, 364)


        # 06_1 AGENT
        self.label06_1.move(43, 396)
        self.edit_result06_1.move(90, 389)
        self.slash_label06_1.move(145, 389)
        self.edit_input06_1.move(160, 389)
        self.lb_g_06_1.move(215, 396)

        # 06_2 RUNNER
        self.label06_2.move(37, 423)
        self.edit_result06_2.move(90, 416)
        self.slash_label06_2.move(145, 416)
        self.edit_input06_2.move(160, 416)
        self.lb_g_06_2.move(215, 423)
        

        # 06_3 채널
        self.label06_3.move(62, 450)
        self.edit_result06_3.move(90, 443)
        self.slash_label06_3.move(145, 443)
        self.edit_input06_3.move(160, 443)
        self.lb_g_06_3.move(215, 450)
        self.lb_result_06.move(243, 437)



        # 06_4 IIP AGENT
        self.label06_4.move(25, 477)
        self.edit_result06_4.move(90, 470)
        self.slash_label06_4.move(145, 470)
        self.edit_input06_4.move(160, 470)
        self.lb_g_06_4.move(215, 477)
        




        # 장기요양
        # 04 점검중
        self.label07.move(50, 550)       # 장기요양 점검중
        self.edit_result07.move(90, 543)
        self.slash_label07.move(145, 543)
        self.edit_input07.move(160, 543)
        self.lb_g_07.move(215, 550)
        self.lb_result_07.move(243, 550)








    # 콤마 추가 함수
    def add_comma(self):
        text = self.sender().text().replace(',', '')  # 콤마 제거
        if text.isdigit():
            formatted_text = '{:,}'.format(int(text))  # 콤마 추가
            self.sender().setText(formatted_text)
        else:
            self.sender().setText('')

if __name__ == '__main__':
    app = QApplication([])
    window = Robot()
    window.show()
    app.exec_()
