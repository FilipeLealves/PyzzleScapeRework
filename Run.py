import pygame as pg, sys, os
from Stage import GameStage

class initial():
    def __init__(self) -> None:
        self.size = screenWidth, screenHeight = 800, 700
        self.screen = pg.display.set_mode(self.size)
        self.white = 255,255,255

initial()
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type ==  pg.QUIT: sys.exit()

    clock.tick(30)
    GameStage(1)
    pg.display.update() 
    