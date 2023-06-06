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
        self.noteMax = 60
        self.noteTimer = 0
        self.sheetTimer = 0
        self.sheetMax = 2
        self.stop = False
        self.currentRotation = 0 
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

        self.sheetTimer += 1
        self.noteTimer += 1
        if not self.stop:
            if self.sheetTimer >= self.sheetMax:
                self.initPlayerTrailSheet()
                self.sheetTimer = 0

            if self.noteTimer >= self.noteMax:
                self.initPlayerTrailNote()
                self.noteTimer = 0

    def loadAssets(self):
        self.playerTrailImg = pyglet.image.load('./assets/MusicNote.png')
        self.playerTrailImg.anchor_x = self.playerTrailImg.width // 2
        self.playerTrailImg.anchor_y = self.playerTrailImg.height // 2 
        self.SheetMusic = pyglet.image.load('./assets/SheetMusicClearThin.png')
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
        if self.currentRotation < self.player.currentRotation:
            self.currentRotation += 2
        elif self.currentRotation > self.player.currentRotation:
            self.currentRotation -= 2
        playerTrailSheetSystem = ParticleSystem(self.player.x, self.player.y, 1, 180, 10, self.SheetMusic, self.playerTrailSheetInitialVelocity, False, False, angle=self.currentRotation)
        #print(self.player.currentRotation)
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
        self.stop = False
        self.particleSystems = []
