import pyglet

class ProgressBar:

    def __init__(self, x, y, colour, maxWidth, maxProgress):
        self.anchorX = x
        self.anchorY = y
        self.colour = colour
        self.progress = 0
        self.maxProgress = maxProgress
        self.maxWidth = maxWidth
        self.borderSize = 20
        self.bar = pyglet.shapes.Rectangle(x=self.anchorX, y=self.anchorY, width=self.maxWidth, height=self.maxWidth/8, color=self.colour)
        self.barOutline = pyglet.shapes.Rectangle(x=self.anchorX, y=self.anchorY, width=self.maxWidth + self.borderSize, height=self.maxWidth/8 + self.borderSize, color=(255, 255, 255))
        self.bar.anchor_x = self.anchorX - self.borderSize/2
        self.bar.anchor_y = self.bar.height/2
        self.barOutline.anchor_y = self.barOutline.height/2
    
    def increment(self, amount):
        self.progress += amount
        if self.progress > self.maxProgress:
            self.progress = self.maxProgress
    
    def reset(self):
        self.progress = 0

    def draw(self):
        self.bar.width = self.maxWidth * (self.progress / self.maxProgress)
        self.barOutline.draw()
        self.bar.draw()