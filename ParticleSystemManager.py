import pyglet
from ParticleSystem import ParticleSystem

class ParticleSystemManager:

    def __init__(self, window):
        self.window = window
        self.particleSystems = []
        self.loadAssets()

    def draw(self):
        for particleSystem in self.particleSystems:
            particleSystem.draw()

    def update(self):
        for particleSystem in self.particleSystems:
            particleSystem.update()
            if(particleSystem.isFinished()):
                self.particleSystems.remove(particleSystem)
    
    def loadAssets(self):
        self.playerExplosionImg = pyglet.image.load('PlayerParticle.png')
    
    def initPlayerExplosion(self, playerX, playerY):
        playerExplosionSystem = ParticleSystem(playerX, playerY, 100, self.playerExplosionImg)
        self.particleSystems.append(playerExplosionSystem)


