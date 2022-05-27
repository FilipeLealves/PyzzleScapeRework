import pygame as pg, sys
from Stage import GameStage

size = screenWidth, screenHeight = 800, 700
screen = pg.display.set_mode(size)
white = 255,255,255

while True:
    for event in pg.event.get():
        if event.type ==  pg.QUIT: sys.exit()
    GameStage(1)  
    pg.display.update()