import sys 
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('프로그램 가동')  # 프로그램 상단 제목
        self.move(300, 300)  # x축, y축
        self.resize(400, 200)  # width, height
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())