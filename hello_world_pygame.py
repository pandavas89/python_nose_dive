import pygame
import sys
from pygame.locals import *

width = 600
height = 400
white = (255, 255, 255)
black = (  0,   0,   0)
fps = 30
stride = 5
x = 0
y = 0

pygame.init()

pygame.display.set_caption('Hello, world!')
displaysurf = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()

gulimfont = pygame.font.SysFont('굴림', 70)
helloworld = gulimfont.render('Hello, world!', 1, black)

hellorect = helloworld.get_rect()
hellorect.center = (width / 2, height / 2)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x += stride
    elif keys[pygame.K_a]:
        x -= stride
    elif keys[pygame.K_w]:
        y -= stride
    elif keys[pygame.K_s]:
        y += stride
    displaysurf.fill(white)
    hellorect.center = (width/2 + x, height /2 + y)
    displaysurf.blit(helloworld, hellorect)

    pygame.display.update()
    clock.tick(fps)
