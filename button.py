import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('button.ui', self)

        # self는 MyApp을 이용해 만든 객체
        #pushButton프로그램 안에서 만들어진 버튼 이름
        # clicked 버튼이 클릭 될 때
        # connect() 이벤트 연결
        self.pushButton.clicked.connect(self.button_click)

        # 객체의 변수
        self.click_count = 0
        self.nametag = "네임태그"

    def button_click(self):
        # 객체의 변수 증가하기
        self.click_count += 1
        # 객체의 위젯에 택스트
        self.pushButton.setText(f"{self.nametag}가 출력되었습니다.")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
