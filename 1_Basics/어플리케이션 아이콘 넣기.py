import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("아이콘!")
        self.setWindowIcon(QIcon(r"C:\Users\admin\Documents\PyQt5_Study\1_Basics\icon.png"))     # 창의 아이콘 설정
        # 뭔진 몰라도 어설픈 상대경로는 이미지를 불러오지 못한다. 일단 절대경로를 사용
        
        # self.move(300, 300)     
        # self.resize(400, 200)   
        self.setGeometry(300, 300, 300, 200)    # 창의 위치, 크기 설정 (move, resize 함수를 합한 역할)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
