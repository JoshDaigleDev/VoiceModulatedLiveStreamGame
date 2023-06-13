from ObstacleManager import ObstacleManager
from PlayerManager import PlayerManager
from ParticleSystemManager import ParticleSystemManager
from TextManager import TextManager
from LaserCannonManager import LaserCannonManager
from LandscapeManager import LandscapeManager
from LiveManager import LiveManager

class Game:

    def __init__(self, window):
        self.window = window
        self.playerManager = PlayerManager(self.window)
        self.obstacleManager = ObstacleManager(self.window)
        self.particleSystemManager = ParticleSystemManager(self.window, self.playerManager.player, self.obstacleManager)
        self.textManager = TextManager(self.window)
        self.laserCannonManager = LaserCannonManager(self.window, self.playerManager, self.particleSystemManager)
        self.landscapeManager = LandscapeManager(self.window)
        self.liveManager = LiveManager()
        self.gameOver = False
        self.gameScore = 0


    def draw(self):
        self.landscapeManager.draw()
        self.particleSystemManager.draw()
        self.obstacleManager.draw()
        self.laserCannonManager.draw()
        self.textManager.draw()
        if not self.gameOver:
            self.playerManager.draw()


    def update(self, dt):
        self.landscapeManager.update()
        self.particleSystemManager.update(dt)
        self.laserCannonManager.update()
        self.textManager.update(str(self.gameScore))
        if not self.gameOver:
            self.obstacleManager.update(dt)
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
        self.particleSystemManager.reset()

        
    def increaseScore(self):
        self.gameScore += 0.5
