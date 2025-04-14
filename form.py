import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget) :

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("프로그램 실행")
        self.move(300, 300)  # 창위치
        self.resize(400, 200) # 창 사이즈
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()  # 객체생성
    sys.exit(app.exec_())