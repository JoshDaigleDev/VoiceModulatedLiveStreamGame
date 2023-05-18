from Particle import Particle
import pyglet
import random
class ParticleSystem:
    def __init__(self, x, y, num, image):
        self.originX = x
        self.originY = y
        self.particles = []
        self.lifeSpan = 120
        self.particleNum = num
        self.image = image
        self.init()

    def init(self):
        self.sprite = pyglet.sprite.Sprite(self.image, x=self.originX, y=self.originY)
        self.sprite.scale = 100 / self.sprite.width
        for i in range(0, self.particleNum):
            xVelocity = random.randint(-50, 50)
            yVelocity = random.randint(-50, 50)
            sprite = pyglet.sprite.Sprite(self.image, x=self.originX, y=self.originY)
            sprite.scale = 25 / sprite.width
            particle = Particle(self.originX, self.originY, self.lifeSpan, sprite, xVelocity, yVelocity)
            self.particles.append(particle)

    def draw(self):
        for particle in self.particles:
            particle.draw()
    
    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.isDead():
                self.particles.remove(particle)
    
    def isFinished(self):
        finished = True
        for particle in self.particles:
            if not particle.isDead():
                finished = False
        
        return finished

        


