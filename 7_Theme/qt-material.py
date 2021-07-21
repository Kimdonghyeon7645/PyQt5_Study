"""
qt-material
> https://github.com/UN-GCPDS/qt-material
> `pip install qt-material` 로 설치
"""
import sys
# from PySide6 import QtWidgets
# from PySide2 import QtWidgets
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet, list_themes


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vb = QVBoxLayout()
        vb.addWidget(QPushButton('버튼'))
        vb.addWidget(QCheckBox('체크박스'))
        vb.addWidget(QLabel('라벨'))
        vb.addStretch()
        self.setLayout(vb)
        self.setWindowTitle('이게... material..?')
        self.setGeometry(300, 300, 400, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(list_themes())
    apply_stylesheet(app, theme='dark_amber.xml')
    ex = MyApp()
    sys.exit(app.exec_())
