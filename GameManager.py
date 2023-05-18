from ObsticleManager import ObsticleManager
from PlayerManager import PlayerManager
from AudioManager import AudioManager
from ParticleSystemManager import ParticleSystemManager

class GameManager:

    def __init__(self, window):
        self.window = window
        self.playerManager = PlayerManager(self.window)
        self.obsticleManager = ObsticleManager(self.window)
        self.particleSystemManager = ParticleSystemManager(self.window)
        self.audioManager = AudioManager()
        self.gameOver = False

    def draw(self):
        self.obsticleManager.draw()
        self.particleSystemManager.draw()
        if not self.gameOver:
            self.playerManager.draw()

    def update(self, dt, pitch, decibles):
        self.particleSystemManager.update()
        if not self.gameOver:
            self.obsticleManager.update(dt)
            movement = self.audioManager.pitchToMovement(pitch, decibles)
            self.playerManager.movePlayer(movement*dt)


    def endGame(self):
        self.gameOver = True
        player = self.playerManager.player
        self.particleSystemManager.initPlayerExplosion(player.x, player.y)

    def reset(self):
        self.gameOver = False
        self.playerManager.reset()
        self.obsticleManager.reset()