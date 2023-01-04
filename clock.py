import pygame
import numpy as np
import os
import time

# 게임 윈도우 크기
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SILVER = (192, 192, 192)



def Rmat(deg):
    radian = np.deg2rad(deg)

    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([[c, -s, 0],[s, c, 0], [0, 0, 1]])
    return R

def Tmat(a,b):
    H = np.eye(3)
    H[0,2] = a
    H[1,2] = b
    return H

def loadImage(img):
    current_path = os.path.dirname(__file__)
    assets_path = os.path.join(current_path, 'assets')

    img_clock = pygame.image.load(os.path.join(assets_path, "clock.png"))
    if img == 'clock':
        return img_clock

pygame.init()

# 윈도우 제목
pygame.display.set_caption("Robot arms")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()


font = pygame.font.SysFont('FixedSys', 80, True, False)
# 게임 종료 전까지 반복
done = False

img_clock = loadImage('clock')
clock_rect = img_clock.get_rect()
clock_rect.center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2)

sec_poly = np.array([[0,0,1],[250,0,1],[250,5,1],[0,5,1]])
min_poly = np.array([[0,0,1],[200,0,1],[200,7,1],[0,7,1]])
hour_poly = np.array([[0,0,1],[150,0,1],[150,10,1],[0,10,1]])

h = time.localtime(time.time()).tm_hour -12
m = time.localtime(time.time()).tm_min
s = time.localtime(time.time()).tm_sec

sdeg = -90 + 6 * s   # strat from current time
mdeg = - 90 + 6 * m
hdeg = - 90 + 30 * h  + m /12 * 6


# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    h = time.localtime(time.time()).tm_hour -12
    m = time.localtime(time.time()).tm_min
    s = time.localtime(time.time()).tm_sec
    

    sdeg += 6   # 6 degree per second
    secH = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2) @ Rmat(sdeg) @Tmat(-2.5,-2.5)
    sec_line = (secH @ sec_poly.T)[0:2].T

    mdeg += 6 / 60  # 6 degree per min = 6 /60 degree per sec
    minH = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2) @ Rmat(mdeg) @Tmat(-3.5,-3.5)
    min_line = (minH @ min_poly.T)[0:2].T

    hdeg += 30 / 3600   #30 degree per hour = 30 /60 degree per min = 30 /3600 degree per sec
    hourH = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2) @ Rmat(hdeg) @Tmat(-5,-5)
    hour_line = (hourH @ hour_poly.T)[0:2].T
    print(h,m,s)
    screen.fill(WHITE)
    
    pygame.draw.polygon(screen,BLACK,sec_line,0)
    pygame.draw.polygon(screen,BLACK,min_line,0)
    pygame.draw.polygon(screen,BLACK,hour_line,0)
    screen.blit(img_clock,clock_rect)




    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(1)

# 게임 종료
pygame.quit()