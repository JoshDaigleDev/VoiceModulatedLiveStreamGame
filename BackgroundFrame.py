import pyglet 
from Mover import Mover
class BackgroundFrame(Mover):
    
    def __init__(self, x, y, image, window):
        self.window = window
        self.x = x
        self.y = y
        self.background = pyglet.sprite.Sprite(img=image, x=self.x, y=self.y)
        self.background.scale = self.window.height / self.background.height
    

    def draw(self):
        self.background.draw()

    def update(self):
        self.background.update(self.x, self.y)
