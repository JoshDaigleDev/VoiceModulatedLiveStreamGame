import pyglet

class ProgressBar:

    def __init__(self, dim, x, y, unitLen, maxProgress, colour):
        self.dim = dim
        self.progress = 0
        self.maxProgress = maxProgress
        self.unitLen = unitLen
        self.width = unitLen * dim.unit
        self.bar = pyglet.shapes.Rectangle(x=x, y=y, width=self.width, height=dim.unit, color=colour)
        self.barOutline = pyglet.shapes.Rectangle(x=x-dim.unit/5, y=y-dim.unit/5, width=self.width + 2/5*dim.unit, height=dim.unit + 2/5*dim.unit, color=(255, 255, 255))

    
    def increment(self, amount):
        self.progress += amount
        if self.progress > self.maxProgress:
            self.progress = self.maxProgress
    

    def reset(self):
        self.progress = 0


    def draw(self):
        self.bar.width = self.width * (self.progress / self.maxProgress)
        self.barOutline.draw()
        self.bar.draw()