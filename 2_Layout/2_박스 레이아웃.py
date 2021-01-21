import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
""" 박스 레이아웃(Box Layout)
QHBoxLayout, QVBoxLayout 등으로 각각 수평, 수직 박스를 만들 수 있음
만든 박스에는 다른 레이아웃 박스를 넣거나 위젯을 배치할 수 있음
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 2개(ok, cance) 생성
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 수평박스(QHBoxLayout) 
        hbox = QHBoxLayout()    # 수평박스 생성 : QHBoxLayout()
        hbox.addStretch(1)      # 신축성있는 빈 공간 제공
        hbox.addWidget(okButton)        # 공간에 버튼 위젯 추가
        hbox.addWidget(cancelButton)    # 공간에 버튼 위젯 추가
        hbox.addStretch(1)      # 빈 공간 제공22, 양 사이드의 빈공간이 서로 동일한 값(1)이기에 두 빈공간은 창의 크기 상관없이 항상 같음

        # 수직박스(QVBoxLayout)
        vbox = QVBoxLayout()    # 수직박스 생성 : QVBoxLayout()
        vbox.addStretch(3)      # 3 빈공간 제공
        vbox.addLayout(hbox)    # 수평박스(hbox)를 수직박스(vbox)에 추가
        vbox.addStretch(1)      # 1 빈공간 제공, 양 사이드의 빈공간이 3과 1이기에 두 빈공간은 창의 크기 상관없이 3:! 비율 유지

        self.setLayout(vbox)    # 수직박스를 창의 메인 레이아웃으로 설정

        self.setWindowTitle('박스레이아웃')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
