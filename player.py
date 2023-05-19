import pyglet
from Mover import Mover

class Player(Mover):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.radius = 50
        self.dead = False

    def draw(self):
        circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(255, 0, 0))
        circle.draw()
        super().draw()

    def update(self):
        self.sprite.update(self.x, self.y-50)
        #square = pyglet.shpaes.rectangle(self.x, self.y, self.radius, self.radius, color=(55, 55, 255))
        #self.playerSprite.draw()

    def reset(self, x, y):
        self.dead = False
        self.x = x
        self.y = y
