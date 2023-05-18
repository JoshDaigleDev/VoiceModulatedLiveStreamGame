from Entity import Entity
class Particle(Entity):

    def __init__(self, x, y, lifeSpan, sprite, xVelocity=0, yVelocity=0):
        super().__init__(x,y)
        self.lifeSpan = lifeSpan
        self.sprite = sprite
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
    
    def draw(self):
        if not self.isDead():
            self.sprite.draw()
    
    def update(self):
        self.move(self.xVelocity, self.yVelocity)
        self.yVelocity += -5
        self.sprite.update(self.x, self.y)
        self.lifeSpan += -1
    
    def isDead(self):
        return self.lifeSpan <= 0
    

