from ObsticleManager import ObsticleManager
from PlayerManager import PlayerManager
from AudioManager import AudioManager
from ParticleSystemManager import ParticleSystemManager
from BackgroundFrameManager import BackgroundFrameManager

class GameManager:

    def __init__(self, window):
        self.window = window
        self.playerManager = PlayerManager(self.window)
        self.obsticleManager = ObsticleManager(self.window)
        self.particleSystemManager = ParticleSystemManager(self.window, self.playerManager.player)
        self.backgroundFrameManager = BackgroundFrameManager(self.window)
        self.audioManager = AudioManager()
        self.gameOver = False

    def draw(self):
        self.backgroundFrameManager.draw()
        self.obsticleManager.draw()
        self.particleSystemManager.draw()
        if not self.gameOver:
            self.playerManager.draw()

    def update(self, dt, pitch, decibles):
        self.particleSystemManager.update()
        self.obsticleManager.update(dt)
        self.backgroundFrameManager.update()
        if not self.gameOver:
            movement = self.audioManager.pitchToMovement(pitch, decibles)
            self.playerManager.movePlayer(movement*dt)


    def endGame(self):
        self.gameOver = True
        self.particleSystemManager.initPlayerExplosion()

    def reset(self):
        self.gameOver = False
        self.playerManager.reset()
        self.obsticleManager.reset()
        self.backgroundFrameManager.reset()
        self.particleSystemManager.reset()
