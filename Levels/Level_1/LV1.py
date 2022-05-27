import os
import pygame as pg
from Player import MainPlayer

size = screenWidth, screenHeight = 800, 700
screen = pg.display.set_mode(size)
white = 0,0,0
player = pg.Rect(230, 129, 35, 60)

class Level_1():
    def __init__(self) -> None:
        screen.blit(pg.image.load(os.path.join('Levels\\Level_1\\img','bg.png')), (0,0))
        MainPlayer(screen, player)
