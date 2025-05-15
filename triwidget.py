import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic # user interface compiler


import os  # os기능을 가져옴


ui_path = os.path.join(os.path.dirname(__file__), "triwidget.ui") # 현재 폴더 경로 가져옴. 


class MyApp(QMainWindow):
    def __init__(self):  # self라는 매개변수는 다른이름으로 써도 되나, 객체 자신이 매개변수이므로 관례적으로 self를 사용
        super().__init__()
        uic.loadUi(ui_path, self)
        self.btn_1.clicked.connect(self.button_click)

    def button_click(self):
        input_text = self.txb_1.text()

        self.lbl_1.setText(input_text)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
