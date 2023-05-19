from Particle import Particle
import pyglet
class ParticleSystem:
    def __init__(self, x, y, num, lifeSpan, size, image, veloctity_generation, external_force):
        self.originX = x
        self.originY = y
        self.particles = []
        self.lifeSpan = lifeSpan
        self.particleNum = num
        self.image = image
        self.size = size
        self.velocity_generation = veloctity_generation
        self.external_force = external_force
        self.init()

    def init(self):
        for i in range(0, self.particleNum):
            xVelocity, yVelocity = self.velocity_generation()
            sprite = pyglet.sprite.Sprite(self.image, x=self.originX, y=self.originY)
            sprite.scale = self.size / sprite.width
            particle = Particle(self.originX, self.originY, self.lifeSpan, sprite, xVelocity, yVelocity)
            self.particles.append(particle)

    def draw(self):
        for particle in self.particles:
            particle.draw()
    
    def update(self):
        for particle in self.particles:
            particle.update(self.external_force)
            if particle.isDead():
                self.particles.remove(particle)
    
    def isFinished(self):
        finished = True
        for particle in self.particles:
            if not particle.isDead():
                finished = False
        
        return finished

        


