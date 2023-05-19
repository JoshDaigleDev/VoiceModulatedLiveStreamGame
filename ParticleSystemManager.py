import pyglet
import random
from ParticleSystem import ParticleSystem

class ParticleSystemManager:

    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.particleSystems = []
        self.loadAssets()
        self.timerMax = 54
        self.playerTrailTimer = self.timerMax
        self.stop = False

    def draw(self):
        for particleSystem in self.particleSystems:
            if particleSystem.size != 25:
                particleSystem.draw()

        for particleSystem in self.particleSystems:
            if particleSystem.size == 25:
                particleSystem.draw()
        
    def update(self):
        for particleSystem in self.particleSystems:
            particleSystem.update()
            if(particleSystem.isFinished()):
                self.particleSystems.remove(particleSystem)

        self.playerTrailTimer -= 1

        if self.playerTrailTimer % 9 == 0 and not self.stop:
            self.initPlayerTrailSheet()
        elif self.playerTrailTimer <= 0:
            self.initPlayerTrailSheet()
            self.initPlayerTrailNote()
            self.playerTrailTimer = self.timerMax

    def loadAssets(self):
        self.playerExplosionImg = pyglet.image.load('./assets/PlayerParticle.png')
        self.playerTrailImg = pyglet.image.load('./assets/MusicNote.png')
        self.SheetMusic = pyglet.image.load('./assets/SheetMusic6.png')
    
    def initPlayerExplosion(self):
        self.stop = True
        playerExplosionSystem = ParticleSystem(self.player.x, self.player.y, 100, 120, 25, self.playerExplosionImg, self.playerExplosionInitialVelocity, self.standardGravity)
        self.particleSystems.append(playerExplosionSystem)
    
    def initPlayerTrailNote(self):
        playerTrailNoteSystem = ParticleSystem(self.player.x, self.player.y, 2, 180, 25, self.playerTrailImg, self.playerTrailNoteInitialVelocity, self.noChange)
        self.particleSystems.append(playerTrailNoteSystem)

    def initPlayerTrailSheet(self):
        playerTrailSheetSystem = ParticleSystem(self.player.x, self.player.y, 1, 210, 10, self.SheetMusic, self.playerTrailSheetInitialVelocity, self.noChange)
        self.particleSystems.append(playerTrailSheetSystem)

    def playerExplosionInitialVelocity(self):
        xVelocity = random.randint(-50, 50)
        yVelocity = random.randint(-50, 50)

        return xVelocity, yVelocity
    
    def playerTrailNoteInitialVelocity(self):
        xVelocity = -1 - random.random() / 5
        yVelocity = random.random()
        
        return xVelocity, yVelocity

    def playerTrailSheetInitialVelocity(self):
        xVelocity = -1
        yVelocity = 0
        
        return xVelocity, yVelocity

    def standardGravity(self, x, y):
        xNew = x
        yNew = y - 5

        return xNew, yNew
    
    def noChange(self, x, y):
        xNew = x
        yNew = y #+ random.random() - 0.3
            
        return xNew, yNew

    def reset(self):
        self.playerTrailTimer = self.timerMax
        self.stop = False
        self.particleSystems = []
