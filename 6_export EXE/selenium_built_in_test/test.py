import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from selenium import webdriver


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

    def open_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
            self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        except Exception as e:
            print(e)

    def close_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
