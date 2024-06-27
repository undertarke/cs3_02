import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((600, 600))


pygame.display.set_caption("Mummy maze !!")

surfaceMap = pygame.transform.scale(
    pygame.image.load("./mummy/image/floor.jpg"), (600, 600))


# (0,0) - (60,0) - (120, 0) - (180 , 0) - (240, 0)

playerUp = pygame.image.load("./mummy/image/player/move_up.png")
playerDown = pygame.image.load("./mummy/image/player/move_down.png")
playerLeft = pygame.image.load("./mummy/image/player/move_left.png")
playerRight = pygame.image.load("./mummy/image/player/move_right.png")

TIME = 5


mummyUp = pygame.image.load("./mummy/image/mummy/redup.png")
mummyDown = pygame.image.load("./mummy/image/mummy/reddown.png")
mummyLeft = pygame.image.load("./mummy/image/mummy/redleft.png")
mummyRight = pygame.image.load("./mummy/image/mummy/redright.png")


class Player:
    mummyGo = False

    def __init__(self):
        self.x = 0
        self.y = 0
        self.surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surface.blit(playerDown, (20, 20), (0, 0, 60, 60))
        self.timeSkip = 0
        self.option = 0

        self.go = 0

    def update(self, up, down, left, right):

        if Player.mummyGo == False:
            if self.go < 100:

                if self.timeSkip <= TIME:  # 0 - 5
                    self.option = 0
                elif self.timeSkip <= TIME*2:  # 6 - 10
                    self.option = 1
                elif self.timeSkip <= TIME*3:  # 11 - 15
                    self.option = 2
                elif self.timeSkip <= TIME*4:
                    self.option = 3
                elif self.timeSkip <= TIME*5:
                    self.option = 4

                elif self.timeSkip > TIME*5:
                    self.timeSkip = 0

                if up or down or left or right:
                    self.surface.fill((0, 0, 0, 0))
                    self.timeSkip += 1
                    self.animate(up, down, left, right)
                    self.go += 5

                if up:
                    self.y -= 5

                elif down:
                    self.y += 5

                elif left:
                    self.x -= 5

                elif right:
                    self.x += 5
            else:
                Player.mummyGo = True
                self.go = 0

    def animate(self, up, down, left, right):
        img = ""
        if up:
            img = playerUp
        elif down:
            img = playerDown
        elif left:
            img = playerLeft
        elif right:
            img = playerRight

        if self.option == 0:
            self.surface.blit(img, (20, 20), (0, 0, 60, 60))
        if self.option == 1:
            self.surface.blit(img, (20, 20), (60, 0, 60, 60))
        if self.option == 2:
            self.surface.blit(img, (20, 20), (120, 0, 60, 60))
        if self.option == 3:
            self.surface.blit(img, (20, 20), (180, 0, 60, 60))
        if self.option == 4:
            self.surface.blit(img, (20, 20), (240, 0, 60, 60))

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))


class Mummy:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.surface.blit(mummyDown, (20, 20), (0, 0, 60, 60))
        self.timeSkip = 0
        self.option = 0

        self.go = 0

    def update(self, up, down, left, right):

        if Player.mummyGo == True:
            if self.go < 100:
        
                if self.timeSkip <= TIME:  # 0 - 5
                    self.option = 0
                elif self.timeSkip <= TIME*2:  # 6 - 10
                    self.option = 1
                elif self.timeSkip <= TIME*3:  # 11 - 15
                    self.option = 2
                elif self.timeSkip <= TIME*4:
                    self.option = 3
                elif self.timeSkip <= TIME*5:
                    self.option = 4

                elif self.timeSkip > TIME*5:
                    self.timeSkip = 0

                if up or down or left or right:
                    self.surface.fill((0, 0, 0, 0))
                    self.timeSkip += 1
                    self.animate(up, down, left, right)
                    self.go += 5

                if up:
                    self.y -= 5

                elif down:
                    self.y += 5

                elif left:
                    self.x -= 5

                elif right:
                    self.x += 5
            else:
                Player.mummyGo = False
                self.go = 0

    def animate(self, up, down, left, right):
        img = ""
        if up:
            img = mummyUp
        elif down:
            img = mummyDown
        elif left:
            img = mummyLeft
        elif right:
            img = mummyRight

        if self.option == 0:
            self.surface.blit(img, (20, 20), (0, 0, 60, 60))
        if self.option == 1:
            self.surface.blit(img, (20, 20), (60, 0, 60, 60))
        if self.option == 2:
            self.surface.blit(img, (20, 20), (120, 0, 60, 60))
        if self.option == 3:
            self.surface.blit(img, (20, 20), (180, 0, 60, 60))
        if self.option == 4:
            self.surface.blit(img, (20, 20), (240, 0, 60, 60))

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, self.y))


def main():
    player = Player()
    mummy = Mummy()

    up, down, left, right = False, False, False, False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up = True
                if event.key == K_DOWN:
                    down = True
                if event.key == K_LEFT:
                    left = True
                if event.key == K_RIGHT:
                    right = True

        DISPLAYSURF.blit(surfaceMap, (0, 0))
        player.draw()
        player.update(up, down, left, right)

        mummy.draw()
        mummy.update(True,down,left,right)

        if player.go == 0:
            up, down, left, right = False, False, False, False

        

        pygame.display.update()
        pygame.time.Clock().tick(60)


main()
