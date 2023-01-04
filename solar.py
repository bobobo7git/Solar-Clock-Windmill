import pygame
import numpy as np
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SILVER = (192, 192, 192)

class Solar:
    def __init__(self, img):
        self.img = loadImage(img)
        self.rect = self.img.get_rect()
        self.per = 365
        self.dist = 0
        self.planet = True
        
        self.deg = 0
        self.d = 0
        self.speed = 0.5

    def update(self, cen = None):
        self.d = 360/self.per * self.speed
        self.deg -= self.d
        if self.planet:
            self.rect.center =  ((Tmat(WINDOW_WIDTH/2,WINDOW_HEIGHT/2) @Rmat(self.deg) @ np.array([self.dist,self.dist,1]).copy().T ).T)[:2]
        else:
            self.rect.center =  ((Tmat(cen.rect.centerx,cen.rect.centery) @Rmat(self.deg) @ np.array([self.dist,self.dist,1]).copy().T ).T)[:2]

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

    img_sun = pygame.image.load(os.path.join(assets_path, "sun.png"))
    img_venus = pygame.image.load(os.path.join(assets_path, "venus.png"))
    img_earth = pygame.image.load(os.path.join(assets_path, "earth.png"))
    img_moon = pygame.image.load(os.path.join(assets_path, "moon.png"))
    img_saturn = pygame.image.load(os.path.join(assets_path, "saturn.png"))
    img_titan = pygame.image.load(os.path.join(assets_path, "titan.png"))

    if img == 'sun':
        return img_sun
    if img == 'venus':
        return img_venus
    if img == 'earth':
        return img_earth
    if img == 'moon':
        return img_moon
    if img == 'saturn':
        return img_saturn
    if img == 'titan':
        return img_titan

sun = Solar('sun')
venus = Solar('venus')
earth = Solar('earth')
moon = Solar('moon')
saturn = Solar('saturn')
titan = Solar('titan')

sun.per = 0
venus.per = 225
earth.per = 365
moon.per = 27
saturn.per = 365 * 29
titan.per = 16

sun.planet = False
venus.planet = True
earth.planet = True
moon.planet = False
saturn.planet = True
titan.planet = False

sun.dist = 0
venus.dist = 100
earth.dist = 200
moon.dist = 50
saturn.dist = 300
titan.dist = 50



# Pygame 초기화
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



# 게임 반복 구간
while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    sun.rect.center = np.array([WINDOW_WIDTH/2,WINDOW_HEIGHT/2])
    

    venus.update()
    earth.update()
    saturn.update()
    moon.update(earth)
    titan.update(saturn)
    
    screen.blit(sun.img, sun.rect)
    screen.blit(venus.img, venus.rect[:2])
    screen.blit(earth.img, earth.rect[:2])
    screen.blit(saturn.img, saturn.rect[:2])
    screen.blit(moon.img, moon.rect[:2])
    screen.blit(titan.img, titan.rect[:2])
    
   


    

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()