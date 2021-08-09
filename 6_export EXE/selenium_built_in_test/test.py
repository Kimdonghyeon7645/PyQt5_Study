from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from selenium import webdriver
import sys
import os


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.driver = None
        self.init_ui()

    def init_ui(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setText("웹 드라이버 열기")
        btn1.clicked.connect(self.open_driver)

        btn2 = QPushButton('Button2', self)
        btn2.setText("웹 드라이버 닫기")
        btn2.clicked.connect(self.close_driver)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)
        self.setWindowTitle('셀레니움 드라이버 열고 닫기')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
            # module 'sys' has no attribute '_MEIPASS'
            # 원래 파이썬에서 그대로 실행하면 위같이 뜨는게 맞다.
            # _MEIPASS 는 pyinstaller 에서 만들어주는 속성이지, 원래 파이썬의 sys 모듈에 있는게 아니다.
            # 출처 https://stackoverflow.com/questions/65865523/module-sys-has-no-meipass-member
        except Exception as e:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def open_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
            chromedriver_path = self.resource_path("chromedriver.exe")
            self.driver = webdriver.Chrome(chromedriver_path, options=options)
        except Exception as e:
            print(e)

    def close_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
