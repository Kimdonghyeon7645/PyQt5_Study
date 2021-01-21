# 모듈 불러오기
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    """ MyApp(위젯 클래스)
    PyQt5의 QWidget 클래스를 상속받아 필요한 구현을 추가/변경해서 사용
    """
    def __init__(self):
        """ 위젯 초기화 """
        super().__init__()      # 부모 클래스(super() = QWidget)의 초기화(__init__())함수 실행
        self.initUI()       # GUI 레이아웃 구성하는 내부 함수를 호출

    def initUI(self):
        """ GUI 레이아웃을 구성하는 내부함수 (이름이 initUI말고, ui_setup같이 자유롭게 써도된다.) """
        self.setWindowTitle("창 이름!")     # 타이틀 바에 쓰이게되는 창의 제목 설정
        self.move(300, 300)     # 창을 스크린의 x=300(px), y=300(px) 위치로 이동
        self.resize(400, 200)   # 크기를 너비 400(px), 높이 200(px) 으로 조절
        self.show()     # 스크린에 보여줌

if __name__ == '__main__':
    """ 실행
    QApplication을 초기화 한 후에 우리가 만든 클래스를 실행한다.
    (sys.argv = 명령줄로 실행했을 때 옵션을 받는 부분)
    """
    app = QApplication(sys.argv)    # 어플리케이션 객체 생성
    ex = MyApp()
    sys.exit(app.exec_())   # exec_로 이벤트 루프를 생성 (창이 종료될 때까지 이벤트 루프는 계속 돌음)
