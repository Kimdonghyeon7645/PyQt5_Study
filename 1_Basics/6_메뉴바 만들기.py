import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon
""" 메뉴바(Menu bar) : 다양한 명령들의 모음이 위치
GUI 어플리케이션에서 흔하게 사용되며, 
macOS에서도 menubar.setNativeMenuBar(False) 코드를 추가함으로써 윈도우 환경과 동일한 결과를 얻을 수 있다.
"""


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('1_Basics/exit.png'), 'Exit', self)   
        # 아이콘(exit.png) 과 라벨(Exit)를 가지는 동작 생성 : Qaction(아이콘객체, "라벨 내용", self)
        exitAction.setShortcut('Ctrl+Q')    # 동작의 단축키(shortcut) 생성 : setShortcut("단축키")
        exitAction.setStatusTip("나가시게?")   # 동작의 상태팁(=툴팁처럼 마우스를 올리면 생기는데 상태바 위치에 텍스트 생김) 생성 : setStatusTip("상태팁 내용")
        exitAction.triggered.connect(qApp.quit)     # 동작을 선택했을 때 생성된 시그널(triggered)이 qApp의 quit 메소드에 연결 -> 어플리케이션을 종료시킴

        self.statusBar()    # 지난번 배운 상태바 생성

        menubar = self.menuBar()    # 메뉴바 생성 : self.menuBar()
        menubar.setNativeMenuBar(False)     # Mac인 경우 이 코드로 Window와 같은 메뉴바로 생성됨
        filemenu = menubar.addMenu('&File') # 메뉴바에 메뉴 생성 : 메뉴바.addMenu("메뉴명")
        # addMenu() 에서 메뉴명 앞에 &(엠퍼센드)가 붙으면 'Alt + 메뉴명의 맨 앞글자'를 해당 메뉴의 단축키로 활용가능
        filemenu.addAction(exitAction)  # 메뉴에 동작 추가 : 메뉴.addAction(동작)

        self.setWindowTitle('메뉴바 맨들어먹기')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())