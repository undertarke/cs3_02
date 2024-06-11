import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Hello Pygame !!")

surface = pygame.Surface((150, 105))

time = 5
timeSkip = 0
option = 0
x = 0
y = 400

url="./pygame/img/kyo.png"

def animate(option,url):
    if option == 5:
        surface.blit(pygame.image.load(url), (0, 0, 150, 105))
    if option == 4:
        surface.blit(pygame.image.load(url), (-150, 0, 150, 105))
    if option == 3:
        surface.blit(pygame.image.load(url), (-290, 0, 150, 105))
    if option == 2:
        surface.blit(pygame.image.load(url), (-430, 0, 150, 105))
    if option == 1:
        surface.blit(pygame.image.load(url), (-570, 0, 150, 105))
    if option == 0:
        surface.blit(pygame.image.load(url), (-720, 0, 150, 105))

left=False
right=False
# vòng lặp game vô tận
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                y -= 150
            if event.key == K_DOWN:
                y += 150
            if event.key == K_LEFT:
                left = True
            if event.key == K_RIGHT:
                right = True

        if event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
    if left:
        timeSkip += 1
        x-=5
        url="./pygame/img/kyo_r.png"
    if right:
        timeSkip += 1
        x+=5
        url="./pygame/img/kyo.png"

    DISPLAYSURF.fill((255, 255, 255))  # Red Green Blue

    surface.fill((0, 0, 0, 0))

   
   
    if timeSkip <= time:  # 0 - 5
        option = 0
    elif timeSkip <= time*2:  # 6 - 10
        option = 1
    elif timeSkip <= time*3:  # 11 - 15
        option = 2
    elif timeSkip <= time*4:
        option = 3
    elif timeSkip <= time*5:
        option = 4
    elif timeSkip <= time*6:
        option = 5

    elif timeSkip > time*6:
        timeSkip = 0

    animate(option,url)

    DISPLAYSURF.blit(surface, (x, y))

    pygame.display.update()
    pygame.time.Clock().tick(60)  # FPS
