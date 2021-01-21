""" 어플리케이션에 날짜와 시간 표시하기
QtCore 모듈 QDate, QTime, QDateTime 클래스 이용
"""

from PyQt5.QtCore import QDate
# QDate 클래스 : 날짜와 관련된 기능들 제공

now = QDate.currentDate()   # 현재 날짜 반환 : currentDate()
print(now.toString())       # 현재 날짜 문자열 출력 : toString()
# 출력 형식 : 목 1 21 2021


# 날짜 형식 변경 : toString() 메소드의 format 매개값을 설정
from PyQt5.QtCore import Qt

now = QDate.currentDate()
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
