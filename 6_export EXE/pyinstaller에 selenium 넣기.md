# selenium 넣는법

### 1. 드라이버 경로 수정

```driver_path = r"대충경로\chromedriver.exe"``` 를 아래와 같이 바꿔준다.
```python
try:
    base_path = sys._MEIPASS
except Exception as e:
    base_path = os.path.abspath(".")
driver_path = os.path.join(base_path, "chromedriver.exe")
```

> 참고로 _MEIPASS 는 원래 파이썬 os 패키지에 없는 속성이다.  
pyinstaller 에서 만들어주는 속성이므로 그냥 파이썬 코드로 실행하면 속성이 없다고 에러난다.

### 2. 실행파일 생성시 옵션 추가

```commandline
pyinstaller --add-binary "chromedriver.exe;." 파일명.py
```

이거다   
> 대가리 깨져도 복붙해서 글쓰는 블로그들이 ```pyinstaller --add-binary "chromedriver.exe";"." 파일명.py``` 와 같이 글 올려서 자꾸 뭔 에러가 났는데, 알고보니 옵션 인자 이상하게 넘겨줬다.