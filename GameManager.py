import pyglet
from ObsticleManager import ObsticleManager
from PlayerManager import PlayerManager
from AudioManager import AudioManager
from CollisionEventDispatcher import CollisionEventDispatcher

class GameManager:

    def __init__(self, window):
        self.window = window
        self.playerManager = PlayerManager(self.window)
        self.obsticleManager = ObsticleManager(self.window)
        self.audioManager = AudioManager()
        self.collisionDetector = CollisionEventDispatcher(self.playerManager, self.obsticleManager)
        CollisionEventDispatcher.register_event_type('collision')

    def draw(self):
        self.window.clear()
        self.playerManager.draw()
        self.obsticleManager.draw()

    def update(self, dt, pitch, decibles):
        self.collisionDetector.detectCollision()
        self.obsticleManager.update(dt)
        movement = self.audioManager.pitchToMovement(pitch, decibles)
        self.playerManager.movePlayer(movement*dt)

