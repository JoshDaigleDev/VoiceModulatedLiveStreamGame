import pyglet
from Mover import Mover

class Obstacle(Mover):
    def __init__(self, x, y, width, height, boundary=False):
        super().__init__(x,y)
        self.width = width
        self.height = height
        self.left = x
        self.right = x + width
        self.top = y + height
        self.bottom = y
        self.boundary = boundary
        self.passed = False
        self.rectangle = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=(0, 0, 0))

    def contains(self, x, y, radius):
        x_distance = abs(x - (self.left + self.width / 2))
        y_distance = abs(y - (self.bottom + self.height / 2))

        if x_distance <= (self.width / 2 + radius) and y_distance <= (self.height / 2 + radius):
            return True
        return False

    def draw(self):
        self.rectangle.draw()        

    def update(self, dx, dy):
        self.move(dx, dy)
        self.rectangle.x = self.x
        self.rectangle.y = self.y
        self.left = self.x
        self.right = self.x + self.width
        self.top = self.y + self.height
        self.bottom = self.y
        self.centerX = (self.right - self.left) / 2
        self.centerY = (self.top - self.bottom) / 2



