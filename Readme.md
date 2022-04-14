# Python 공부

나도코딩 님의 [파이썬 코딩 무료 강의 (활용편1)](https://www.youtube.com/watch?v=Dkx8Pl6QKW0&t=97s)을 보면서 작성하였습니다.

## 설치

```bash
pip install pygame
```

## 코딩

### 초기화

```py
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
```

### FPS

```py
# FPS
clock = pygame.time.Clock()
dt = clock.tick(30)
```
