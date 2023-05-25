from Particle import Particle
import pyglet
class ParticleSystem:
    def __init__(self, x, y, num, lifeSpan, size, image, veloctity_generation, externalForce, bounce):
        self.originX = x
        self.originY = y
        self.particles = []
        self.lifeSpan = lifeSpan
        self.particleNum = num
        self.image = image
        self.sequence = False
        if isinstance(self.image, pyglet.image.ImageGrid):
            self.sequence = True
        self.size = size
        self.velocity_generation = veloctity_generation
        self.externalForce = externalForce
        self.bounce = bounce
        self.init()

    def init(self):
        for i in range(0, self.particleNum):
            xVelocity, yVelocity = self.velocity_generation()
            if self.sequence:
                imageFragment = self.image[i]
                imageFragment.anchor_x = imageFragment.width // 2 
                imageFragment.anchor_y = imageFragment.height // 2 
                sprite = pyglet.sprite.Sprite(img=imageFragment, x=self.originX, y=self.originY)
                sprite.scale = (2 * self.size ) / sprite.width
            else:
                sprite = pyglet.sprite.Sprite(img=self.image, x=self.originX, y=self.originY)
                sprite.scale = self.size / sprite.width
            particle = Particle(self.originX, self.originY, self.lifeSpan, sprite, self.size, self.bounce, xVelocity, yVelocity)
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

        


