# 모듈 불러오기
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("창 이름!")     # 타이틀 바에 쓰이게되는 창의 제목 설정
        self.move(300, 300)     # 창을 스크린의 x=300(px), y=300(px) 위치로 이동
        self.resize(400, 200)   # 크기를 너비 400(px), 높이 200(px) 으로 조절
        self.show()     # 스크린에 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv)    # 어플리케이션 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())
