import pyglet
from Mover import Mover

class Obstacle(Mover):
    def __init__(self, dim, x, y, width, height, rendering=None, top=False, sprite=None, boundary=False):
        super().__init__(x,y)
        self.dim = dim
        self.width = width
        self.height = height

        self.boundary = boundary
        self.passed = False

        self.alpha = 255
        
        self.sprite = sprite

        self.left = x
        self.right = x + width
        self.top = y + height
        self.bottom = y
        self.isTop = top

        if boundary:
            batch = rendering[0]
            ordering = rendering[1]
            self.rectangle = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=(0, 0, 0), batch=batch, group=ordering[7])


    def contains(self, x, y, radius):
        x_distance = abs(x - (self.left + self.width / 2))
        y_distance = abs(y - (self.bottom + self.height / 2))

        if x_distance <= (self.width / 2 + radius) and y_distance <= (self.height / 2 + radius):
            return True
        return False


    def update(self, dx, dy):
        self.move(dx, dy)
        if self.passed:
            if self.isTop:
                self.move(0, self.height/120)
            else: 
                self.move(0, -self.height/120)
        
        if self.boundary:
            self.rectangle.x = self.x
            self.rectangle.y = self.y
        else:
            self.sprite.update(self.x, self.y)

        self.left = self.x
        self.right = self.x + self.width
        self.top = self.y + self.height
        self.bottom = self.y
        self.centerX = (self.right - self.left) / 2
        self.centerY = (self.top - self.bottom) / 2



