import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
""" 메인창(Main window) : 메뉴바, 툴바, 상태바를 갖는 전형적인 어플리케이션 창
메인창은 고유의 레이아웃을 가지고 있다.

- Menu Bar (QMenuBar) : 맨 윗쪽 끝 ㅡ자 영역
- Status Bar (QStatusBar) : 맨 아래쪽 끝 ㅡ자 영역
- Toolbars (QToolBar) : 가운데 영역을 감싸는 ㅁ자 영역
- Dock Widgets (QDockWidget) : Toolbars 영역 안에서, Central Widget을 감싸는 ㅁ자 영역
- Central widget : 중심 위젯, 어떠한 위젯도 들어올 수 있음
"""


""" 상태바(status bar) : 어플리케이션의 상태를 알려주기 위해 어플리케이션 맨 하단에 위치하는 위젯
QStatusBar = 상태바 객체

상태바 생성하기
    - QMainWindow 클래스의 statusBar() 메소드 이용 
        (최초 메소드 호출 이후에는 상태바 객체(QStatusBar) 반환)

상태바에 텍스트 표시하기 
    - showMessage() 메소드 이용

텍스트 사라지게 하기 
    - clearMessage() 메소드 이용
    - showMessage() 메소드에서 텍스트 표시 시간을 설정

현재 상태바에 표시되는 메시지 텍스트 가져오기
    - currentMessage() 메소드 이용

상태바에 표시되는 메시지 변경시마다 = QStatusBar 클래스가 messageChanged() 시그널 발생
"""


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('안녕 상태바!')
        print(self.statusBar())
        # QMainWindow 클래스의 statusBar() 메소드로 상태바 생성
        # QStatusBar 클래스의 showMessage() 메소드로 상태바에 보여질 메시지 설정

        self.setWindowTitle('상태바 만들어먹기') 
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
