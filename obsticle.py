import pyglet
from entity import Entity

class Obsticle(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x,y)
        self.width = width
        self.height = height

    def draw(self):
        #print(self.x, self.y)
        square = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=(255, 255, 255))
        square.draw()

    


