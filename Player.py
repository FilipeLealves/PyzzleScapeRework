import pygame as pg
import os

load = pg.image.load
path = 'Player\\img'
pathSound = 'Player\\sound'
walkCount = 0

class MainPlayer():
    def __init__(self, screen, player) -> None:
        self.player = player
        self.vel = 5
        self.screen = screen
        self.left = False
        self.up = False
        self.down = False
        self.right = False
        self.stand = False
        self.walkLeft = [load(os.path.join(path,'L1.png')),load(os.path.join(path,'L2.png')),load(os.path.join(path,'L3.png')),load(os.path.join(path,'L4.png')),load(os.path.join(path,'L5.png')),load(os.path.join(path,'L6.png')),load(os.path.join(path,'L7.png')),load(os.path.join(path,'L8.png')),load(os.path.join(path,'L9.png'))]
        self.walkRight = [load(os.path.join(path,'R1.png')),load(os.path.join(path,'R2.png')),load(os.path.join(path,'R3.png')),load(os.path.join(path,'R4.png')),load(os.path.join(path,'R5.png')),load(os.path.join(path,'R6.png')),load(os.path.join(path,'R7.png')),load(os.path.join(path,'R8.png')),load(os.path.join(path,'R9.png'))]
        self.walkUp = [load(os.path.join(path,'U1.png')),load(os.path.join(path,'U2.png')),load(os.path.join(path,'U3.png')),load(os.path.join(path,'U4.png')),load(os.path.join(path,'U5.png')),load(os.path.join(path,'U6.png')),load(os.path.join(path,'U7.png')),load(os.path.join(path,'U8.png')),load(os.path.join(path,'U9.png'))]
        self.walkDown = [load(os.path.join(path,'D1.png')),load(os.path.join(path,'D2.png')),load(os.path.join(path,'D3.png'))]
        self.standUp = [load(os.path.join(path,'S1.png')),load(os.path.join(path,'S2.png')),load(os.path.join(path,'S3.png')),load(os.path.join(path,'S4.png')),load(os.path.join(path,'S5.png')),load(os.path.join(path,'S6.png')),load(os.path.join(path,'S7.png'))]
        self.draw()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.player.y -= self.vel
            self.up = True
        elif keys[pg.K_s]:
            self.player.y += self.vel
            self.down = True
        elif keys[pg.K_a]:
            self.player.x -= self.vel
            self.left = True
        elif keys[pg.K_d]:
            self.player.x += self.vel
            self.right = True
        else:
            self.stand = True

    def draw(self):
        self.move()
        self.animation()

    def animation(self):
        global walkCount
        if walkCount + 1 >= 27:
            walkCount = 0

        if self.left:   #LEFT
            self.screen.blit(self.walkLeft[walkCount//3], (self.player.x, self.player.y))
            walkCount += 1
        elif self.right:#RIGHT
            self.screen.blit(self.walkRight[walkCount//3], (self.player.x, self.player.y))
            walkCount += 1
        elif self.up:   #UP
            self.screen.blit(self.walkUp[walkCount//3], (self.player.x, self.player.y))
            walkCount += 1
        elif self.down: #DOWN
            self.screen.blit(self.walkDown[walkCount//9], (self.player.x, self.player.y))
            walkCount += 3
        else:           #STAND
            self.screen.blit(self.standUp[walkCount//9], (self.player.x, self.player.y))
            walkCount += 1