import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
""" 절대적 배치(Absolute positoning) : 각 위젯 위치와 크기를 픽셀 단위로 설정해서 배치
상대적인 다른 레이아웃과 다른 절대적인 기준으로 배치

절대적 배치 특)
- 창의 크기를 조절해도 위젯의 크기와 위치는 고정
- 다양한 플랫폼에서 어플리케이션이 다르게 보일 수 있음
- 어플리케이션 폰트 변경시 레이아웃 망가질 수 있음
- 레이아웃 수정하려면 완전 새로 고쳐야 되서 번거로움
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 라벨 2개 생성하고 배치
        QLabel('Label1', self).move(20, 20)
        QLabel('Label2', self).move(20, 60)

        # 버튼 2개 생성하고 배치
        QPushButton('Button1', self).move(80, 13)
        QPushButton('Button2', self).move(80, 53)

        self.setWindowTitle('절대배치')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())