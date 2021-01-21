import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))    # 먼저 툴팁에 사용할 폰트 설정 : setFont(QFont("폰트이름", 폰트크기(px)))

        self.setToolTip('요건 <b>QWidget</b>의 툴팁 <small>입니다!</small>')  # self(= MyApp = 기본 창 위젯)에 툴팁 생성 : setToolTip("표시될 html") 
        # self.setToolTip('<img src="image_data/icon.png">')    # 툴팁은 이미지도 된다 ^^ (html 기반이라 웬만한 태그 다먹음)

        btn = QPushButton('Button', self)   # 푸쉬버튼 생성
        btn.setToolTip('요고슨 <p style="color:red;">QPushButton</p><p>의 <mark>툴팁</mark> 입니다!</p>')   # 푸쉬버튼에 툴팁 생성
        btn.move(50, 50)
        btn.resize(btn.sizeHint())  # btn.sizeHint() -> 버튼을 적당한 크기로 설정하도록 도외줌

        self.setWindowTitle('툴팁 만들어먹기')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())