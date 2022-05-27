import os
import pygame

size = screenWidth, screenHeight = 800, 700
screen = pygame.display.set_mode(size)
white = 0,0,0

class Level_2():
    def __init__(self) -> None:
        #pygame.image.load(os.path.join('IMG','LV1_BACKGROUND.png'))
        screen.blit(pygame.image.load(os.path.join('Levels\\Level_2\\img','bg.png')), (0,0))