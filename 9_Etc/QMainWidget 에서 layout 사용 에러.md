# QWainWidget 에선 LayOut을 쓸 수 없다

> 참고 : https://freeprog.tistory.com/326

![image](https://user-images.githubusercontent.com/48408417/119757490-fc036f00-bedf-11eb-8d8e-44cce91004a3.png)

```1_Basics/4_상태바 만들기.py```에서 사용한 **QMainWidget**은 메뉴바, 툴바, 상태바 등을 지원하는 프레임워크같은 위젯이다.  
이 **QMainWidget**은 위 사진처럼 고유의 레이아웃을 가지고 있는데, 

> #### QMainWidget 의 고유 레이아웃 
> 
> - Menu Bar (QMenuBar) : 맨 윗쪽 끝 ㅡ자 영역
> - Status Bar (QStatusBar) : 맨 아래쪽 끝 ㅡ자 영역
> - Toolbars (QToolBar) : 가운데 영역을 감싸는 ㅁ자 영역
> - Dock Widgets (QDockWidget) : Toolbars 영역 안에서, > Central Widget을 감싸는 ㅁ자 영역
> - Central widget : 중심 위젯, 어떠한 위젯도 들어올 수 있음

여기서 *Central Widget*을 ```2_Layout```에서 배운 *QHBoxLayout, QVBoxLayout* 으로 레이아웃을 지정할 수 있을까? 

결론은 **Central Widget은 self.setCentralWidget(위젯)으로 위젯을 지정한다. 바로 레이아웃을 지정할 수 없다**  
따라서, setCentralWidget() 에 들어갈 위젯 클래스(=*QWidget*을 상속)를 만들고, 그 위젯 클래스를 인자로 넘겨줘야 된다.  
그렇기에 setCentralWidget() 의 인자로 넘겨줄 위젯 클래스에 QHBoxLayout과 같은 레이아웃을 지정해주면, 우리가 기대하던 ***Central Widget*을 레이아웃을 지정할 수 있다**

