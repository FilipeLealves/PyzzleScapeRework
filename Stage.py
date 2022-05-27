from Levels.Level_1.LV1 import Level_1
from Levels.Level_2.LV2 import Level_2

class GameStage():
    def __init__(self, levelNumber):
        self.stage = levelNumber
        self.stageManager()
        
    def stageManager(self):
        if self.stage == 0:
            pass                  
        if self.stage == 1:
            Level_1()
        if self.stage == 2:
            Level_2()