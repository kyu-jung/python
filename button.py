import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic # user interface compiler


import os  # os기능을 가져옴


ui_path = os.path.join(os.path.dirname(__file__), "button.ui") # 현재 폴더 경로 가져옴. 


class MyApp(QMainWindow):

    def __init__(self):  # self라는 매개변수는 다른이름으로 써도 되나, 객체 자신이 매개변수이므로 관례적으로 self를 사용
        super().__init__()
        uic.loadUi(ui_path, self)

        self.btn3text = self.btn_3.text()
        self.btn2text = self.btn_2.text()
        # self.버튼이름.clicked.connect(self.메서드) -> 클릭할때 메서드 발동
        self.btn_1.clicked.connect(self.button_click) # 디자인된 모습을 코드를 수정하여 실시간으로 수정할 수 있다.
        self.btn_3.clicked.connect(self.get_text)


    def button_click(self):
        self.btn_1.setText("클릭했습니다")


    def get_text(self):

        if self.btn3text != self.btn_2.text():
            self.btn_2.setText(self.btn3text)
        elif self.btn2text != self.btn_2.text():
            self.btn_2.setText(self.btn2text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

# 1. anaconda prompt에서 designer 검색
# 2. Qt Designer에서 drag and drop으로 간편하게 디자인
# 3. 속성 부분에서 objectName, Text 등 수정 가능
# 4. 