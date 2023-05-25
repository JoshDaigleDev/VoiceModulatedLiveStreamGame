from ObstacleManager import ObstacleManager
from PlayerManager import PlayerManager
from AudioManager import AudioManager
from ParticleSystemManager import ParticleSystemManager
from BackgroundFrameManager import BackgroundFrameManager
from TextManager import TextManager

class GameManager:

    def __init__(self, window):
        self.window = window
        self.playerManager = PlayerManager(self.window)
        self.obstacleManager = ObstacleManager(self.window)
        self.particleSystemManager = ParticleSystemManager(self.window, self.playerManager.player)
        self.backgroundFrameManager = BackgroundFrameManager(self.window)
        self.textManager = TextManager(self.window)
        self.audioManager = AudioManager()
        self.gameOver = False
        self.gameScore = 0

    def draw(self):
        self.backgroundFrameManager.draw()
        self.particleSystemManager.draw()
        self.obstacleManager.draw()
        if not self.gameOver:
            self.playerManager.draw()
        if not self.obstacleManager.settingUp:
            self.textManager.draw()

    def update(self, dt, pitch, decibles):
        self.particleSystemManager.update()

        self.textManager.update(str(self.gameScore))
        if not self.gameOver:
            self.obstacleManager.update(dt)
            self.backgroundFrameManager.update()
            movement, direction = self.audioManager.pitchToMovement(pitch, decibles)
            self.playerManager.movePlayer(movement*dt, direction)

    def endGame(self):
        self.gameOver = True
        self.particleSystemManager.initPlayerExplosion(self.playerManager.playerImage)

    def reset(self):
        self.gameOver = False
        self.gameScore = 0
        self.playerManager.reset()
        self.obstacleManager.reset()
        self.backgroundFrameManager.reset()
        self.particleSystemManager.reset()

    def increaseScore(self):
        self.gameScore += 1
