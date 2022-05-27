import os
import pygame as pg
from Player import MainPlayer

size = 800, 700
screen = pg.display.set_mode(size)
player = pg.Rect(230, 129, 35, 60)
switchLight = False
switchNum = 0

pg.init()
pg.mixer.init()

path = 'Levels\\Level_1\\sounds'
click = pg.mixer.Sound(os.path.join(path,'click.wav'))
 
pos = (127, 168, 1, 365), (127, 125, 520, 1),(490, 150, 200, 1),(127,532,550,1),(675,250,1,280), (646,169,1,80),(646,248,50,1),(116,436,44,80)

class Level_1():
    def __init__(self) -> None:
        self.bg_on = pg.image.load(os.path.join('Levels\\Level_1\\img','bg_on.png'))
        self.bg_off = pg.image.load(os.path.join('Levels\\Level_1\\img','bg_off.png'))
        self.walls()
        self.events()
    
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

    def showPlayer(self, visible):
        self.visible = visible 
        if(self.visible == True):
            MainPlayer(screen, player)
        else:
            MainPlayer(screen, player)

    def events(self):
        global switchLight, switchNum
        self.visible = True
        self.chair = pg.Rect(568, 193, 30, 30)
        self.lightSwitch = pg.Rect(300,140,10,10)
        
        switchNum+=1

        #TURN OFF AND ON OF LIGHT   
        keys = pg.key.get_pressed()
        if player.colliderect(self.lightSwitch) and keys[pg.K_SPACE] and switchNum > 10 and switchLight == False:
            switchLight = True
            switchNum = 0
            click.play()

        elif player.colliderect(self.lightSwitch) and keys[pg.K_SPACE] and switchNum > 10 and switchLight == True:
            switchLight = False
            switchNum = 0
            click.play()

        if switchLight == True:
            screen.blit(self.bg_on, (0,0))
        else:
            screen.blit(self.bg_off, (0,0))
        
        if switchNum > 10:
            switchNum = 10

        self.chairImg = pg.image.load(os.path.join('Levels\\Level_1\\img','chair.png'))

        if player.colliderect(self.chair):
            #self.standBack = pg.image.load(os.path.join('Levels\\Level_1\\img','stand_back.png'))
            #screen.blit(self.standBack, (player.x, player.y))
            self.visible = False
        
        if (self.visible == True):
            self.showPlayer(True)
        else:
            self.showPlayer(False)

        screen.blit(self.chairImg,(550, 193))

    