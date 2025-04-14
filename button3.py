import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget

class MyApp(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('button3.ui', self)

        self.btn_1.clicked.connect(self.button_click)
        self.btn_2.clicked.connect(self.button_click2)
        self.btn_3.clicked.connect(self.button_click3)

        btn_new = QpushButton("새로운 버튼", self)
        btn_new.setCheckable(True)

        btn_old = QpushButton("옛날 버튼", self)
        btn_old.setEnabled(False)

        # 객체의 변수
        self.click_count = 0
        self.nametag = "네임태그"
        self.again = "다음에도 만들어 주세요"
        self.Double = "두배"

    def button_click(self):
        # 객체의 변수 증가하기
        self.click_count += 1
        # 객체의 위젯에 텍스트
        self.btn_1.setText(f"{self.again}가 출력되었습니다.")
    
    def button_click2(self):
        # 객체의 변수 증가하기
        self.click_count += 1
        # 객체의 위젯에 텍스트
        self.btn_2.setText(f"{self.Double}가 출력되었습니다.")
    
    def button_click3(self):
        # 객체의 변수 증가하기
        self.click_count += 1
        # 객체의 위젯에 텍스트
        self.btn_3.setText(f"{self.nametag}가 출력되었습니다.")
        

    # 버튼을 클릭했을때
    # 변수 하나 만들어서 원하는 글자가 버튼에 나오도록 만들기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())