from Mover import Mover
class Particle(Mover):

    def __init__(self, x, y, lifeSpan, sprite, xVelocity=0, yVelocity=0):
        super().__init__(x, y, sprite)
        self.lifeSpan = lifeSpan
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
    
    def draw(self):
        if not self.isDead():
            super().draw()
    
    def update(self, force):
        self.move(self.xVelocity, self.yVelocity)
        self.xVelocity, self.yVelocity = force(self.xVelocity, self.yVelocity)
        self.sprite.update(self.x, self.y)
        self.lifeSpan += -1
    
    def isDead(self):
        return self.lifeSpan <= 0
    

