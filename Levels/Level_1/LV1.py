import os
import pygame as pg
from Player import MainPlayer

size = 800, 700
screen = pg.display.set_mode(size)
player = pg.Rect(230, 129, 35, 60)


pos = (127, 168, 1, 365), (127, 125, 520, 1),(490, 150, 200, 1),(127,532,550,1),(675,250,1,280), (646,169,1,80),(646,248,50,1),(116,436,44,80)

class Level_1():
    def __init__(self) -> None:
        screen.blit(pg.image.load(os.path.join('Levels\\Level_1\\img','bg.png')), (0,0))
        MainPlayer(screen, player)
        self.walls()
        self.objects()
    
    def walls(self):
        for i in range(len(pos)):
            wall = pg.Rect(pos[i])
            #pg.draw.rect(screen, (124,252,0), (wall)) #PAREDE VISIVEL
            collision_tolerance = 13
            if player.colliderect(wall):
                if abs(wall.top - player.bottom) < collision_tolerance:
                    player.y -= 5
                if abs(wall.bottom - player.top) < collision_tolerance:
                    player.y += 5
                if abs(wall.right - player.left) < collision_tolerance:
                    player.x += 5
                if abs(wall.left - player.right) < collision_tolerance:
                    player.x -= 5
    
    def objects(self):
        chair = pg.Rect(568, 193, 30, 30)
        self.chairImg = pg.image.load(os.path.join('Levels\\Level_1\\img','chair.png'))
        screen.blit(self.chairImg,(550, 193))