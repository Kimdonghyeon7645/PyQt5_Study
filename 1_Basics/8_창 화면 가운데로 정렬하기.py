import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('가운데 정렬')
        self.resize(500, 350)
        self.center()   # 수제 메소드 center() 호출 
        self.show()

    def center(self):
        qr = self.frameGeometry()   # 창의 위치와 크기 정보를 가져옴
        cp = QDesktopWidget().availableGeometry().center()      # 사용하는 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)   # 창의 위치를 화면의 중심 위치로 이동 : 창위치정보.moveCenter(모니터화면위치)
        self.move(qr.topLeft())     # 실제 창위치를 이동


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())