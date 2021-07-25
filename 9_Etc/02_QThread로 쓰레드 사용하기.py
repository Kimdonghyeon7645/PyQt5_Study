# https://www.da-hae.kr/pyqt5-qthread-%EC%82%AC%EC%9A%A9%EB%B2%95/
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore  # QtCore를 명시적으로 보여주기 위해


class TestThread(QThread):
    # 쓰레드의 커스텀 이벤트
    # 데이터 전달 시 형을 명시해야 함
    threadEvent = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__()
        self.n = 0
        self.main = parent
        self.isRun = False

    def run(self):
        while self.isRun:
            print('쓰레드 : ' + str(self.n))

            # 'threadEvent' 이벤트 발생
            # 파라미터 전달 가능(객체도 가능)
            self.threadEvent.emit(self.n)

            self.n += 1
            self.sleep(1)


class TestGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.btn1 = QPushButton("쓰레드 시작", self)
        self.btn2 = QPushButton("쓰레드 정지", self)
        vertBox = QVBoxLayout()
        vertBox.addWidget(self.btn1)
        vertBox.addWidget(self.btn2)
        self.setLayout(vertBox)
        self.setGeometry(700, 500, 300, 100)

        self.btn1.clicked.connect(self.threadStart)
        self.btn2.clicked.connect(self.threadStop)

        self.show()

        # 쓰레드 인스턴스 생성
        self.th = TestThread(self)

        # 쓰레드 이벤트 연결
        self.th.threadEvent.connect(self.threadEventHandler)

    @pyqtSlot()
    def threadStart(self):
        if not self.th.isRun:
            print('메인 : 쓰레드 시작')
            self.th.isRun = True
            self.th.start()

    @pyqtSlot()
    def threadStop(self):
        if self.th.isRun:
            print('메인 : 쓰레드 정지')
            self.th.isRun = False

    # 쓰레드 이벤트 핸들러
    # 장식자에 파라미터 자료형을 명시
    @pyqtSlot(int)
    def threadEventHandler(self, n):
        print('메인 : threadEvent(self,' + str(n) + ')')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = TestGUI()
    app.exec_()
