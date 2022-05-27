import pygame as pg
import  os

class MainPlayer():
    def __init__(self, screen, player) -> None:
        self.player = player
        self.vel = 5
        self.playerImg = pg.image.load(os.path.join('Levels\\Level_1\\img','stand.png'))
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