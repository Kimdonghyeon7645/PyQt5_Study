import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
""" 라벨(QLabel)
사용자와 상호작용하지 않고 텍스트, 이미지를 띄우는 위젯
텍스트는 수평방향으론 왼쪽, 수직방향으론 가운데가 기본 정렬(setAlignment() 메소드로 재지정 가능)

QLabel 클래스로 생성 (공식 문서 - https://doc.qt.io/qt-5/qlabel.html)
"""


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        label1 = QLabel('으뜸 라벨', self)
        # 라벨 생성 : QLabel("라벨에 표시될 텍스트", 부모 위젯(클래스))
        label1.setAlignment(Qt.AlignCenter)
        # 라벨 배치 설정 : setAlignment(정렬방식)   (Qt.AlignCenter = 가운데 정렬)

        label2 = QLabel('버금 라벨', self)
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()
        # 폰트 생성 : font()
        font1.setPointSize(20)
        # 폰트 크기 설정 : setPointSize(크기)   (디폴트 크기 = 13)

        font2 = label2.font()
        font2.setFamily('Times New Roman')  
        # 폰트 종류 설정 : setFamily("폰트 종류")
        font2.setBold(True)
        # 폰트 진하게 설정 : setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('나의 라벨을 알까?')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
