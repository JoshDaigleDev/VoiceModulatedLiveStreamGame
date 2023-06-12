import pyglet
from Mover import Mover

class Player(Mover):
    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.radius = sprite.image.width/2
        self.rotationAmount = 15
        self.dead = False
        self.currentRotation = 0
        self.rotationIncrement = 0

    def draw(self):
        super().draw()
        #circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(255, 0, 0, 50))
        #circle.draw()

    def move(self, x, y, direction):
        super().move(x,y)
        self.currentRotation = direction * self.rotationAmount
        
        if self.sprite.rotation < self.currentRotation:
            self.rotationIncrement += 0.5
        elif self.sprite.rotation > self.currentRotation:
            self.rotationIncrement -= 0.5
        self.sprite.rotation = self.rotationIncrement


    def reset(self, x, y):
        self.dead = False
        self.x = x
        self.y = y
