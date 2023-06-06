from ObstacleManager import ObstacleManager
from PlayerManager import PlayerManager
from AudioManager import AudioManager
from ParticleSystemManager import ParticleSystemManager
from BackgroundFrameManager import BackgroundFrameManager
from TextManager import TextManager
from LaserCannonManager import LaserCannonManager
from LandscapeManager import LandscapeManager
class GameManager:

    def __init__(self, window):
        self.window = window
        self.playerManager = PlayerManager(self.window)
        self.obstacleManager = ObstacleManager(self.window)
        self.particleSystemManager = ParticleSystemManager(self.window, self.playerManager.player)
        self.backgroundFrameManager = BackgroundFrameManager(self.window)
        self.textManager = TextManager(self.window)
        self.laserCannonManager = LaserCannonManager(self.window, self.playerManager, self.particleSystemManager)
        self.landscapeManager = LandscapeManager(self.window)
        self.audioManager = AudioManager()
        self.gameOver = False
        self.gameScore = 0

    def draw(self):
        #self.backgroundFrameManager.draw()
        self.landscapeManager.draw()
        self.particleSystemManager.draw()
        self.obstacleManager.draw()
        self.laserCannonManager.draw()
        self.textManager.draw()
        if not self.gameOver:
            self.playerManager.draw()
            pass

    def update(self, dt, pitch, decibles):
        self.landscapeManager.update()
        self.particleSystemManager.update()
        self.laserCannonManager.update()
        self.textManager.update(str(self.gameScore))
        if not self.gameOver:
            self.obstacleManager.update(dt)
            #self.backgroundFrameManager.update()
            movement, direction = self.audioManager.pitchToMovement(pitch, decibles)
            self.playerManager.movePlayer(movement*dt, direction)
        if self.laserCannonManager.fired:
            self.endGame()

    def endGame(self):
        if not self.gameOver:
            self.particleSystemManager.initPlayerExplosion(self.playerManager.playerImage)
        self.gameOver = True
        self.laserCannonManager.reset()


    def startLaser(self):
        self.laserCannonManager.start_laser()

    def reset(self):
        self.gameOver = False
        self.gameScore = 0
        self.playerManager.reset()
        self.obstacleManager.reset()
        self.backgroundFrameManager.reset()
        self.particleSystemManager.reset()
        
    def increaseScore(self):
        self.gameScore += 0.5
