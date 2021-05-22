import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("아이콘!")
        self.setWindowIcon(QIcon("image_data/icon.png"))     # 창의 아이콘 설정
        """
        FIX 상대경로로 icon.png 이랬는데 이미지가 깨져서 일단 절대경로를 사용했었다.
        근데 후에 깨달은 것은 상대경로의 기준이 이 파일의 위치가 아니라, 프로젝트 루트 폴더의 위치였다! 
        """
        
        # self.move(300, 300)     
        # self.resize(400, 200)   
        self.setGeometry(300, 300, 300, 200)    # 위치와 크기 설정하기 : setGeometry() ; 위의 move, resize 함수 2개를 합한것과 똑같은 역할을 한다.
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
