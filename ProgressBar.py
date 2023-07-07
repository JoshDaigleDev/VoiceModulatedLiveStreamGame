import pyglet

class ProgressBar:

    def __init__(self, dim, x, y, unitLen, maxProgress, hard=False):
        self.dim = dim
        self.progress = 0
        self.maxProgress = maxProgress
        self.unitLen = unitLen
        self.width = unitLen * dim.unit
        self.red = (255, 0, 0, 255)
        self.yellow = (255, 255, 0, 255)
        self.green = (0, 255, 0, 255)
        self.blue = (0, 255, 255)
        self.color = self.red
        self.bar = pyglet.shapes.Rectangle(x=x, y=y, width=self.width, height=dim.unit, color=self.color)
        self.barBG = pyglet.shapes.Rectangle(x=x, y=y, width=self.width, height=dim.unit, color=(255, 255, 255))
        self.barOutline = pyglet.shapes.Rectangle(x=x-dim.unit/5, y=y-dim.unit/5, width=self.width + 2/5*dim.unit, height=dim.unit + 2/5*dim.unit, color=(237, 10, 187))
        self.hard = hard
        if self.hard:
            self.bar.scale_x = -1

    
    def increment(self, amount):
        if not self.hard:
            self.progress += amount
            if self.progress > self.maxProgress:
                self.progress = self.maxProgress
            
            progressPercent = self.progress / self.maxProgress

            if progressPercent >= 1:
                self.color = self.blue
            elif progressPercent >= 0.70:
                self.color = self.green
            elif progressPercent >= 0.4:
                self.color = self.yellow
            else:
                self.color = self.red
            
            self.bar.color = self.color
    
    def setAmount(self, amount):
        self.progress = amount
        

    def reset(self):
        self.progress = 0


    def draw(self):
        self.bar.width = self.width * (self.progress / self.maxProgress)
        self.barOutline.draw()
        self.barBG.draw()
        self.bar.draw()
