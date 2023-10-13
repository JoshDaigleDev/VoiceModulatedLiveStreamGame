from Mover import Mover
import pyglet
class Particle(Mover):

    def __init__(self, x, y, lifeSpan, sprite, radius, bounce, xVelocity=0, yVelocity=0, rotation=None):
        super().__init__(x, y, sprite)
        self.lifeSpan = lifeSpan
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.radius = radius
        self.bounce = bounce
        self.rotation = rotation
    

    def draw(self):
        if not self.isDead():
            super().draw()

    
    def update(self):
        self.move(self.xVelocity, self.yVelocity)
        self.sprite.update(self.x, self.y)
        if self.rotation:
            self.sprite.rotation = self.rotation
        self.lifeSpan += -1
    
    
    def isDead(self):
        return self.lifeSpan <= 0
    

