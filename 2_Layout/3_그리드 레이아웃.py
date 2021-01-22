import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)
""" 그리드 레이아웃(Grid Layout)
위젯 공간을 행(row)과 열(column)로 구분하는 레이아웃 (가장 일반적인 방법)
QGirdLayout 클래스로 레이아웃 생성
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()    # 그리드 레이아웃 생성 : QGridLayout()
        self.setLayout(grid)    # 어플리케이션 창의 메인 레이아웃으로 설정 

        grid.addWidget(QLabel('Title:'), 0, 0)      # 그리드 레이아웃에 위젯 추가 : addWidget(위젯, 행, 열)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle('그리드레이아웃')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
