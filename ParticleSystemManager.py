import pyglet
import random
from ParticleSystem import ParticleSystem
from ParticleSystem import LaserSystem

class ParticleSystemManager:

    def __init__(self, window, player):
        self.window = window
        self.player = player
        self.particleSystems = []
        self.loadAssets()
        self.timerMax = 54
        self.playerTrailTimer = self.timerMax
        self.stop = False
        self.lasers = LaserSystem()

    def draw(self):
        for particleSystem in self.particleSystems:
            if particleSystem.size == 10 and not self.stop:
                particleSystem.draw()

        for particleSystem in self.particleSystems:
            if particleSystem.size != 10:
                particleSystem.draw()
        
        self.lasers.draw()
        
    def update(self):
        for particleSystem in self.particleSystems:
            particleSystem.update()
            if(particleSystem.isFinished()):
                self.particleSystems.remove(particleSystem)

        self.lasers.update()

        self.playerTrailTimer -= 1

        if self.playerTrailTimer % 9 == 0 and not self.stop:
            self.initPlayerTrailSheet()
        elif self.playerTrailTimer <= 0 and not self.stop:
            self.initPlayerTrailSheet()
            self.initPlayerTrailNote()
            self.playerTrailTimer = self.timerMax

    def loadAssets(self):
        self.playerExplosionImg = pyglet.image.load('./assets/SingleNote.png')
        self.playerTrailImg = pyglet.image.load('./assets/SingleNote.png')
        self.playerTrailImg.anchor_x = self.playerTrailImg.width // 2
        self.playerTrailImg.anchor_y = self.playerTrailImg.height // 2 
        self.SheetMusic = pyglet.image.load('./assets/SheetMusic.png')
        self.SheetMusic.anchor_x = self.SheetMusic.width // 2
        self.SheetMusic.anchor_y = self.SheetMusic.height // 2 
    
    def initPlayerExplosion(self, image):
        self.stop = True
        imageSeq = pyglet.image.ImageGrid(image, 12, 12)
        playerExplosionSystem = ParticleSystem(self.player.x, self.player.y, 144, 600, 6, imageSeq, self.playerExplosionInitialVelocity, True, True)
        self.particleSystems.append(playerExplosionSystem)
        for system in self.particleSystems:
            if system.bounce:
                system.external_force = self.standardGravity
    
    def initPlayerTrailNote(self):
        playerTrailNoteSystem = ParticleSystem(self.player.x, self.player.y, 1, 180, 25, self.playerTrailImg, self.playerTrailNoteInitialVelocity, False, True)
        self.particleSystems.append(playerTrailNoteSystem)

    def initPlayerTrailSheet(self):
        playerTrailSheetSystem = ParticleSystem(self.player.x, self.player.y, 1, 210, 10, self.SheetMusic, self.playerTrailSheetInitialVelocity, False, False)
        self.particleSystems.append(playerTrailSheetSystem)

    def playerExplosionInitialVelocity(self):
        xVelocity = random.randint(-50, 50)
        yVelocity = random.randint(-50, 50)

        return xVelocity, yVelocity
    
    def fire_laser(self, laser):
        self.lasers.add(laser)
    
    def playerTrailNoteInitialVelocity(self):
        xVelocity = -1 - random.random() / 5
        yVelocity = random.random() / 2
        
        return xVelocity, yVelocity

    def playerTrailSheetInitialVelocity(self):
        xVelocity = -1
        yVelocity = 0
        
        return xVelocity, yVelocity

    def standardGravity(self, x, y):
        xNew = x
        yNew = y - 1.5

        return xNew, yNew
    
    def noChange(self, x, y):
        xNew = x
        yNew = y 
            
        return xNew, yNew

    def reset(self):
        self.playerTrailTimer = self.timerMax
        self.stop = False
        self.particleSystems = []
