import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
""" 툴바(Tool bar) 
자주 사용하는 명령들을 더 편리하게 사용할 수 있게 나열해두는 영역
"""


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('1_Basics/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('나가실려?')
        exitAction.triggered.connect(qApp.quit)
        # 지난번 메뉴바처럼 종료 동작(Action)을 생성

        self.statusBar()    # 상태바도 전처럼 생성

        self.toolbar = self.addToolBar('Exit')  # 툴바 생성 : self.addToolBar("툴바명") (툴팁 내용에 툴바명이 쓰이는 듯) 
        self.toolbar.addAction(exitAction)      # 툴바에 동작 등록

        self.setWindowTitle('툴바 맨들어묵기')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())