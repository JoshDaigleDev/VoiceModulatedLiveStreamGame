import pyglet
from Mover import Mover

class Player(Mover):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.radius = 50
        self.rotationAmount = 15
        self.dead = False

    def draw(self):
        super().draw()
        #circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(255, 0, 0, 50))
        #circle.draw()

    def update(self):
        self.sprite.update(self.x, self.y)

    def move(self, x, y, direction):
        super().move(x,y)
        rotation = direction * self.rotationAmount
        self.sprite.rotation = rotation

    def reset(self, x, y):
        self.dead = False
        self.x = x
        self.y = y
