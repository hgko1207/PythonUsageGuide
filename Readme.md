# Python 공부

유튜브 나도코딩 님의 파이썬 코딩 무료 강의 활용편을 보면서 작성하였습니다.

## 설치

```bash
pip install pygame
```

## 1. 게임 만들기

### 초기화

```py
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
```

## 2. GUI 만들기

- Button
- Lable
- Text
- Listbox
- Checkbox
- Radiobutton
- Combobox
- Progressbar
- Menu
- Messagebox
- Frame
- Scrollbar
- Grid

```bash
# 설치
pip install Pillow
pip install keyboard
```

```py
# 예제
from tkinter import *

root = Tk()
root.title("Ko GUI")
root.geometry("640x480") # 가로 * 세로

btn = Button(root, text="버튼")
btn.pack()

label = Label(root, text="안녕하세요")
label.pack()

txt = Text(root, width=30, height=5)
txt.pack()
```

# 3. 웹 스크래핑

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
```

## 정규식

참고할 정규식 사이트

- https://www.w3schools.com/python/python_regex.asp
- https://docs.python.org/ko/3/library/re.html

```py
# 1. re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)
```
