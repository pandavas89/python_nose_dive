import pygame
#윈도우 크기를 결정합니다
size = width, height = 800,600
win = pygame.display.set_mode(size)

#png 리소스를 불러옵니다 : script를 이용하는 경우 working directory 문제로 작동하지 않을 수 있음
bg = pygame.transform.rotozoom(pygame.image.load('freetileset/png/BG/BG.png'),0,0.85)
char1 = pygame.transform.rotozoom(pygame.image.load('freeknight/png/Walk (1).png'),0,0.35)
char2 = pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('freeknight/png/Walk (1).png'),True, False),0,0.35)

#배경을 표시합니다
win.blit(bg,(0,0))
pygame.display.update()
pygame.init()
clock = pygame.time.Clock()

def loadSprite(action, direction):
    spriteList = []
    for i in range(1, 11):
        if (direction == "R"):
            spriteList.append(pygame.transform.rotozoom(pygame.image.load('freeknight/png/%s (%d).png' %(action, i)), -5, 0.35))
        elif (direction =="L"):
            spriteList.append(pygame.transform.rotozoom(pygame.transform.flip(pygame.image.load('freeknight/png/%s (%d).png' %(action ,i)),True, False),1,0.35))

    return spriteList

# 오른쪽을 공격하는 스프라이트
attackRight = loadSprite("Attack", "R")

# 오른쪽으로 걷는 스프라이트
walkRight = loadSprite("Walk", "R")

#왼쪽으로 걷는 스프라이트
walkLeft = loadSprite("Walk","L")

vel = 10
jump = 20
yvel = 0
x = 50
y = 350
left = False
right = False
attack = False
atkcount = 0
walkcount = 0
stopd = True

# 화면을 갱신(redraw)합니다
def redrawG():
    global walkcount
    win.blit(bg, (0, 0))

    # walkCount를 초기화합니다
    if walkcount >= 32:
        walkcount = 0

    # 오른쪽으로 걸을 때
    if right:
        win.blit(walkRight[walkcount//4],(x,y))
        print(walkcount//4)
        walkcount += 1

    # 왼쪽으로 걸을 때
    elif left:
        win.blit(walkLeft[walkcount//4],(x,y))
        walkcount += 1
    # 오른쪽을 보고 멈춰 있을 때
    elif stopd :
        win.blit(char1, (x, y))
        print("Right Direction")
    # 왼쪽을 보고 멈춰 있을 때
    else:
        win.blit(char2, (x,y))
        print("Left Direction")
        pass
    pygame.display.update()

run = True

while run:
    clock.tick(48)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if right:
                right = False
                stopd = True
            if left:
                left = False
                stopd = False
            pass

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if x > width - 100:
            x = width - 100
        x += vel
        right = True
        left = False
    if keys[pygame.K_LEFT]:
        if x < -150:
            x = -150
        x -= vel
        right = False
        left = True
    if keys[pygame.K_UP]:
        if y < 500 and yvel == 0:
            yvel -= jump
    if keys[pygame.K_SPACE]:
        attack = True

    if yvel != 0:
        y += yvel
        yvel += 10
        if y > 500:
            y = 500
            yvel = 0
    print(y, yvel)

    redrawG()

pygame.quit()
