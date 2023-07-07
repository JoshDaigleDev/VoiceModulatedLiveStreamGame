from ProgressBar import ProgressBar

class ProgressBarManager:
    def __init__(self, dim):
        self.dim = dim
        self.showLikeBar = True
        self.showHardBar = False
        self.hideLikeTimer = 0
    
    def initLikeBar(self, goal):
        unit = self.dim.unit
        maxUnits = 30
        x = -12*unit
        y = -9*unit
        self.likeBar = ProgressBar(self.dim, x, y, maxUnits, goal)
    
    def initHardBar(self, duration):
        unit = self.dim.unit
        maxUnits = 28
        x = -12*unit
        y = -9*unit
        self.hardBar = ProgressBar(self.dim, x, y, maxUnits, duration, True)

    def draw(self):
        if self.showLikeBar and self.hideLikeTimer <= 0:
            self.likeBar.draw()
        if self.showHardBar:
            self.hardBar.draw()
    
    def update(self):
        if self.hideLikeTimer > 0:
            self.hideLikeTimer -= 1
    
    def hideLikeBar(self, duration):
        self.hideLikeTimer = duration
    
    def resetLikes(self):
        self.likeBar.reset()
    