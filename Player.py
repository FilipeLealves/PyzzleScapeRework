import pygame as pg
import  os

class MainPlayer():
    def __init__(self, screen, player, playerImg) -> None:
        self.player = player
        self.vel = 5
        self.playerImg = playerImg
        self.screen = screen
        self.draw()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.player.y -= self.vel 
        elif keys[pg.K_s]:
            self.player.y += self.vel
        elif keys[pg.K_a]:
            self.player.x -= self.vel
        elif keys[pg.K_d]:
            self.player.x += self.vel

    def draw(self):
        self.move()
        self.screen.blit(self.playerImg, (self.player.x, self.player.y))