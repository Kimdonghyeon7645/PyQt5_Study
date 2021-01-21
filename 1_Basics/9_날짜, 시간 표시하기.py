""" 어플리케이션에 날짜와 시간 표시하기
QtCore 모듈 QDate, QTime, QDateTime 클래스 이용
"""

# QDate 클래스 : 날짜
from PyQt5.QtCore import QDate

now = QDate.currentDate()   # 현재 날짜 반환 : currentDate()
print(now.toString())       # 현재 날짜 문자열 출력 : toString()


# 날짜 형식 변경 : toString() 메소드의 format 매개값을 설정
from PyQt5.QtCore import Qt

print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))     # ISO 표준 형식
print(now.toString(Qt.DefaultLocaleLongDate))   # 어플리케이션의 기본 설정
""" 출력 결과
21.1.21
21.01.2021
목.1월.2021
2021-01-21
2021년 1월 21일 목요일
"""



# QTime 클래스 : 시간
from PyQt5.QtCore import QTime

# 메소드 형식은 QDate와 동일
time = QTime.currentTime()  
print(time.toString())

# 시간 형식도 마찬가지로 변경 가능
from PyQt5.QtCore import Qt

print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))
""" 출력 결과
15.43.28
15.43.28
15.43.28.576
오후 3:43:28
시계를 보니 오후 3시 43분 입니다    # 컴퓨터 시계 형식 설정을 이상하게 해놔서 이렇게 됨 ^^;;
"""



# QDateTime 클래스 : 날짜 + 시간
from PyQt5.QtCore import QDateTime

# 메소드 형식은 언답무용입니다
datetime = QDateTime.currentDateTime()
print(datetime.toString())

# 날짜+시간 형식도 언답무용
from PyQt5.QtCore import QDateTime, Qt

print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))
""" 출력 결과
21.1.21 15:47:34
21.01.2021, 15:47:34
2021년 1월 21일 목요일 오후 3:47:34
오늘도 즐거운 2021년 01월 21일 시계를 보니 오후 3시 47분 입니다
"""



## 응용 : 상태 표시줄에 날짜와 시간 표시하기
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.datetime = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleShortDate))

        self.setWindowTitle('상태표시줄을 보시오')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())