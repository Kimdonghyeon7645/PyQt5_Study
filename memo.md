# 아직 정리하지 않은 내용 모음

- PyQt의 실행순서
![좋은자료다](https://wikidocs.net/images/page/5222/r16.04.png)

- 메인창(Main Window)의 레이아웃
![이것도 그러다](https://user-images.githubusercontent.com/48408417/105280948-616fe800-5bee-11eb-8bcd-3bd926c8e845.png)

- QtDesigner 로 디자인하듯이 데스크탑앱 만들기
[링크](https://martinii.fun/156)

- QtDesigner 로 디자인한 ui 사용법
    - .ui -> .py : ```pyside6-uic <UI파일 경로> -o <변환할 파일명(.py)>``` or ```pyqt5uic <UI파일 경로> -o <변환할 파일명(.py)>```
    - .ui 를 .py 안에서 불러오기 : ```Ui_MainWindow, QtBaseClass = uic.loadUiType('경로\파일명.ui')```
    
- pyinstaller 에 ui 파일 포함하기 
[링크](https://kwonkyo.tistory.com/534)

- pyinstaller 에 셀레니움 포함하기
[]()
