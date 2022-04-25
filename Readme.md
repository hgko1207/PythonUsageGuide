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
