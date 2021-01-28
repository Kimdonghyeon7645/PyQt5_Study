import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
""" 푸쉬버튼(PushButton) = 명령버튼(command button)
: 사용자의 명령에 따라 프로그램이 어떤 동작을 할 때 사용되는 버튼
GUI 프로그래밍에서 가장 중요하고 흔하게 사용됨

QPushButton 클래스로 생성 (공식 문서 - https://doc.qt.io/qt-5/qpushbutton.html)

- 자주 쓰이는 메소드
setCheckalbe() : True 인자값 넘길시, 누른 상태와 누르지 않은 상태를 유지
toggle() : 상태 변경
setIcon() : 버튼 아이콘 설정
setEnabled() : False 인자값 넘길시, 버튼 사용 불가
isChecked() : 버튼 선택 여부를 반환
setText() : 버튼에 표시될 텍스트 설정
text() : 버튼에 표시된 텍스트 반환

- 자주 쓰이는 시그널
clicked() : 버튼 클릭시 발생
pressed() : 버튼 눌렸을 때 발생
released() : 눌린 버튼을 땔 때 발생
toggled() : 버튼 상태가 바뀔 때 발생
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)    
        # 푸시 버튼 생성 : QPushButton("버튼에 표시될 텍스트", 버튼이 속한 부모 클래스) 
        # 버튼에 단축키 지정할려면, 텍스트 앞에 &(엠퍼센드) 붙이면 'Alt + &뒤의 텍스트' 로 단축키가 설정됨 (여기선 'Alt + b')
        btn1.setCheckable(True)     # 선택, 선택하지 않은 상태를 유지 : setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')    
        # 버튼 텍스트 설정 : setText("버튼에 표시될 텍스트")
        # 버튼 텍스트를 생성 후에 지정 가능

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)      # 버튼 사용 불가능 설정 : setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('나의 푸쉬버튼을 알까?')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
