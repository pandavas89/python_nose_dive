import pygame
#윈도우 크기를 결정합니다
size = width, height = 800,600
win = pygame.display.set_mode(size)

#png 리소스를 불러옵니다 : script를 이용하는 경우 working directory 문제로 작동하지 않을 수 있음
bg = pygame.transform.rotozoom(pygame.image.load('freetileset/png/BG/BG.png'),0,0.85)

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

# 공격하는 스프라이트
attackRight = loadSprite("Attack", "R")
attackLeft = loadSprite("Attack", "L")
# 걷는 스프라이트
walkRight = loadSprite("Walk", "R")
walkLeft = loadSprite("Walk","L")
# 정지 스프라이트
idleRight = loadSprite("Idle", "R")
idleLeft = loadSprite("Idle", "L")
# 달리기 스프라이트
runRight = loadSprite("Run", "R")
runLeft = loadSprite("Run", "L")

vel = 10
rvel = 20
jump = 70
yvel = 0
x = 50
y = 350
left = False
right = False
attack = False
running = False
atkcount = 0
walkcount = 0
spriteCount = 0
stopd = True

# 화면을 갱신(redraw)합니다
def redrawG():
    global walkcount
    global spriteCount
    win.blit(bg, (0, 0))

    # walkCount를 초기화합니다
    if walkcount >= 30:
        walkcount = 0
    if spriteCount >= 30:
        spriteCount = 0

    # 오른쪽으로 걸을 때
    if right:
        if running:
            win.blit(runRight[walkcount//3], (x,y))
        else:
            win.blit(walkRight[walkcount//3],(x,y))
        walkcount += 1
        spriteCount = 0

    # 왼쪽으로 걸을 때
    elif left:
        if running:
            win.blit(runLeft[walkcount//3], (x,y))
        else:
            win.blit(walkLeft[walkcount//3],(x,y))
        walkcount += 1
        spriteCount = 0
    # 오른쪽을 보고 멈춰 있을 때
    elif stopd :
        win.blit(idleRight[spriteCount//3], (x,y))
        spriteCount += 1
        walkCount = 0
    # 왼쪽을 보고 멈춰 있을 때
    else:
        win.blit(idleLeft[spriteCount//3], (x,y))
        spriteCount += 1
        walkCount = 0
        pass
    pygame.display.update()

run = True

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                pass
        if event.type == pygame.KEYUP:
            if right:
                right = False
                stopd = True
            if left:
                left = False
                stopd = False
            pass

    if (y < 350):
        yvel += 9
        y += yvel
        if y > 350:
            y = 350
            yvel = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if x > width - 100:
            x = width - 100
        if running:
            x += rvel
        else:
            x += vel
        right = True
        left = False
    if keys[pygame.K_LEFT]:
        if x < -150:
            x = -150
        if running:
            x -= rvel
        else:
            x -= vel
        right = False
        left = True

    if keys[pygame.K_UP]:
        if y == 350 and yvel == 0:
            yvel -= jump
            y -= 10

    if keys[pygame.K_SPACE]:
        running = True
    else:
        running = False

    print(y, yvel)

    redrawG()

pygame.quit()
