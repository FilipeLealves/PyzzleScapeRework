import os
import pygame
import Run

class Level_1():
    def __init__(self) -> None:
        #pygame.image.load(os.path.join('IMG','LV1_BACKGROUND.png'))
        pygame.display.set_mode(800,700).blit(pygame.image.load(os.path.join('IMG','LV1_BACKGROUND.png')), (0,0))