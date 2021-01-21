import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication   # QtCore 에서 QCoreApplication 모듈 불러오기
"""
창 닫는 것은 걍 띄운 창 맨 오른쪽 위에있는 X를 클릭하면된다.
근데 이번엔 시그널(signal)과 슬롯(slot)을 맛뵈면서 프로그래밍으로 창을 닫는 버튼을 만들어보자.
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)     # 푸쉬버튼 만들기 : QPushButton("버튼에 표시될 텍스트", 버튼이 위치할 부모 위젯) ; 이후에 자세히 다룸
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        """
        PyQt5 이벤트 처리 : 시그널, 슬롯으로 구성.
        btn 을 클릭하면 clicked 시그널이 만들어지고,  
        시그널을 connect(메소드이름) 함수로, 메소드와 연결(connect)하는데, 
        QCoreApplication 의 .instance() 로 인스턴스를 반환해서, 인스턴스의 quit(=어플리케이션을 종료하는) 메소드로 연결한다.
        """

        self.setWindowTitle('닫는 버튼 만들어먹기')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
