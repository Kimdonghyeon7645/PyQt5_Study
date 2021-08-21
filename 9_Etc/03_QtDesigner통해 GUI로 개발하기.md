# QtDesigner를 통해 GUI로 개발하기

Qt를 쓰면서 처음에는 몰랐지만, 알면서 많이 편해진 것이 있다.  
바로, **QtDesigner** 를 이용해 드래그 앤 드롭으로 UI를 개발할 수 있는 점이다.

[노마드 코더의 No-Code 영상](https://www.youtube.com/watch?v=2pPK2DjfaJc&t=103s) 에서처럼,  
디자인 하듯이 UI를 개발할 수 있는 툴이 Qt에선 *Qt Designer*라는 것이다.


## 실행

![image](https://user-images.githubusercontent.com/48408417/130710371-3324e7f7-044b-4933-97f7-166bbc204d59.png)

보통 PyQt, PySide를 설치했으면, 라이브러리 폴더(```파이썬폴더\Library\bin```, ```파이썬폴더\Lib\site-packages\PySide6```)에 알아서 깔려있다.  
찾기 귀찮으면, 윈도우 검색에서 `designer` 라고 치면 나온다.

![image](https://user-images.githubusercontent.com/48408417/130710596-cc7801d0-0912-4329-a5e7-4d046b571b12.png)

클릭해서 실행하면 위같이 시작화면이 뜬다. *Main Window* 가 선택돼있는 것을 확인한 후 *[생성]*을 누르면, 알아서 MainWindow 위젯이 생성된다.

## 사용

<!-- ![녹화_2021_08_25_10_54_19_832](https://user-images.githubusercontent.com/48408417/130713816-4001c6c9-d532-48a5-bcab-5799201a0250.gif) -->
![녹화_2021_08_25_11_02_14_478](https://user-images.githubusercontent.com/48408417/130714905-a968925d-4c29-4e69-9f19-64100bd54a2a.gif)

위같이 드래그랑 드롭으로 위젯을 배치하고, 상세한 속성이나 값들은 클릭하거나 오른쪽 사이드바를 통해 변경할 수 있다.

![image](https://user-images.githubusercontent.com/48408417/130711772-bff49923-757b-4ea0-be37-51b4021b8cf8.png)

**[폼 > 미리보기]** 를 클릭해서 실제 데스크탑 앱이 실행될 모습도 볼 수 있고,

![image](https://user-images.githubusercontent.com/48408417/130711839-25c2b508-5c6e-4b60-8d6b-773b56a2af17.png)

**[폼 > 코드보기]** 를 클릭하면 지금 만든 UI를 코드로 변환할 수 있다.  
근데 변환하는 코드가 C++이라서, 파이썬에서 쓸려면 .ui 파일로 저장한 후에 2가지 방법을 통해 사용한다. 

#### 1. .ui 를 .py 로 변환 

```commandline
pyside6-uic <UI파일 경로> -o <변환할 파일명(.py)>``` or ```pyqt5uic <UI파일 경로> -o <변환할 파일명(.py)>
``` 

#### 2. .ui 를 .py 에서 로드

```python
import sys
from PyQt4 import QtGui, uic

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mywindow.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
```

다른 메소드를 사용하면 불러온 ui파일의 위젯을 반환한다. 이걸 변수에 담아 사용할 수도 있다.

```python
Ui_MainWindow, QtBaseClass = uic.loadUiType('경로\파일명.ui')
```
