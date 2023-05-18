import pyglet
from Entity import Entity

class Obsticle(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x,y)
        self.width = width
        self.height = height
        self.left = x
        self.right = x + width
        self.top = y + height
        self.bottom = y

    def draw(self):
        square = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=(255, 255, 255))
        square.draw()        

    def move(self, dx, dy):
        super().move(dx, dy)
        self.left = self.x
        self.right = self.x + self.width
        self.top = self.y + self.height
        self.bottom = self.y


