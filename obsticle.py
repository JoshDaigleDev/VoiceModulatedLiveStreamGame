import pyglet
from Mover import Mover

class Obsticle(Mover):
    def __init__(self, x, y, width, height, boundary=False):
        super().__init__(x,y)
        self.width = width
        self.height = height
        self.left = x
        self.right = x + width
        self.top = y + height
        self.bottom = y
        self.boundary = boundary

    def draw(self):
        square = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=(0, 0, 0))
        square.draw()        

    def update(self, dx, dy):
        self.move(dx, dy)
        self.left = self.x
        self.right = self.x + self.width
        self.top = self.y + self.height
        self.bottom = self.y



