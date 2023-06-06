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
        #circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(255, 0, 0, 100))
        #circle.draw()
    
    def update(self):
        self.move(self.xVelocity, self.yVelocity)
        self.sprite.update(self.x, self.y)
        """        if self.rotation:
            if self.sprite.rotation < self.rotation:
                self.sprite.rotation += 0.1
            elif self.sprite.rotation > self.rotation:
                self.sprite.rotation -= 0.1"""
        if self.rotation:
            self.sprite.rotation = self.rotation
            #print(self.rotation)
        self.lifeSpan += -1
    
    def isDead(self):
        return self.lifeSpan <= 0
    

