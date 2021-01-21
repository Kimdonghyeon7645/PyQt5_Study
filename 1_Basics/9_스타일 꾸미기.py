import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
""" setStyleSheet()
어플리케이션의 많은 구성 요소 스타일을 자유롭게 변경 가능
setStyleSheet() 메소드에 매개값으로, CSS와 비슷한 스타일 속성값이 문자열로 들어감

Qt의 스타일 시트 문서 : https://doc.qt.io/qt-5/stylesheet-reference.html
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QLable 클래스로 3개의 라벨 위젯 생성
        lbl_red = QLabel('Red여')
        lbl_green = QLabel('Green이래')
        lbl_blue = QLabel('Blue여?')

        # 각 라벨 위젯에다가 스타일 시트 적용
        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        # 수직박스 레이아웃(QVBoxLayout()) 으로 3개 라벨 위젯을 수직으로 배치
        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('색깔놀이 맨들어묵기')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
