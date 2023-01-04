import pygame
import numpy as np


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
SKYBLUE = (135,206,235)



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


pygame.init()

# 윈도우 제목
pygame.display.set_caption("Robot arms")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()


font = pygame.font.SysFont('FixedSys', 40, True, False)
# 게임 종료 전까지 반복
done = False

fan = np.array([[0,0,1],[0,200,1],[250,110,1],[250,90,1]])  #3x4
fan = fan.T
deg1 = 90
deg2 = 210
deg3 = -30



# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 윈도우 화면 채우기
    screen.fill(WHITE)
    
    H1 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2-100) @ Rmat(deg1) @Tmat(-250,-100)
    fan1 = ((H1 @ fan))[0:2].T
    H2 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2-100) @ Rmat(deg2) @Tmat(-250,-100)
    fan2 = ((H2 @ fan))[0:2].T
    H3 = Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2-100) @ Rmat(deg3) @Tmat(-250,-100)
    fan3 = ((H3 @ fan))[0:2].T
    deg1 += 1
    deg2 += 1
    deg3 += 1
    rect = pygame.Rect(WINDOW_WIDTH/2-90,WINDOW_HEIGHT/2-50,180,500)
    pygame.draw.circle(screen,(193,154,107),[WINDOW_WIDTH/2,WINDOW_HEIGHT/2-50],90,0)
    pygame.draw.rect(screen,(96,59,43),rect)
    pygame.draw.circle(screen,(0,71,180),[WINDOW_WIDTH/2,WINDOW_HEIGHT/2-100],30,0)
    pygame.draw.polygon(screen,SKYBLUE,fan1)
    pygame.draw.polygon(screen,SKYBLUE,fan2)
    pygame.draw.polygon(screen,SKYBLUE,fan3)
    pygame.draw.circle(screen,(80,144,160),[WINDOW_WIDTH/2,WINDOW_HEIGHT/2-100],15,0)


    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()