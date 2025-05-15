import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('button1', self) # 변수(objectName) = 위젯('텍스트', self)
        btn1.setCheckable(True) # 체크여부 True 가능, False 불가능
        btn1.toggle()  # 현재 상태 바꿈

        btn2 = QPushButton(self)  # 생성만 한 상태,  화면에 아이콘만 가져다 놓은 상태
        btn2.setText("버튼2") # 텍스트 변경

        btn3 = QPushButton('버튼3', self)
        btn3.setEnabled(False)  # 위젯의 활성화 True 사용가능 False 사용불가

        vbox = QVBoxLayout()  # 레이아웃 생성
        vbox.addWidget(btn1)  # 레이아웃 안에 위젯 포함(추가)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('버튼 위젯 연습')
        self.setGeometry(300, 300, 300, 300)  # x, y, 너비, 높이
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())