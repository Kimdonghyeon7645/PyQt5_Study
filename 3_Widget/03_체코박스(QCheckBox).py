import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt
""" 체크박스(CheckBox)
체크 on/off 두가지 상태를 가지는 버튼

QCheckBox 클래스는 체크박스와, 텍스트 라벨을 같이 제공 (공식 문서 - https://doc.qt.io/qt-5/qbuttongroup.html)

- 자주 쓰이는 메소드
text() : 체크 박스의 라벨 텍스트를 반환
setText() : 체크 박스의 라벨 텍스트를 설정
isChecked() : 체크 박스의 두가지 중 상태를 반환 (True/False)
checkState() : 체크 박스의 세가지 중 상태를 반환 (2/1/0)
toggle() : 체크 박스의 상태를 변경

- 자주 쓰이는 시그널
pressed() : 체크 박스를 누를 때 발생
released() : 누른 체크 박스를 뗄 때 발생
clicked() : 체크 박스를 클릭할 때 발생
stateChanged() : 체크 박스의 상태가 바뀔 때 발생
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
