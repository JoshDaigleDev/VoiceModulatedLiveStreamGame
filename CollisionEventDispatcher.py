import pyglet
import math

class CollisionEventDispatcher(pyglet.event.EventDispatcher):
    def __init__(self, playerManager, obsticleManager):
        self.obsticleManager = obsticleManager
        self.playerManager = playerManager
    
    def detectCollision(self):
        playerX = self.playerManager.player.x
        playerY = self.playerManager.player.y
        playerRadius = self.playerManager.player.radius

        for obsticle in self.obsticleManager.obsticles:
            nearX = max(obsticle.left, min(playerX, obsticle.right))
            nearY = max(obsticle.bottom, min(playerY, obsticle.top))

            distance = math.sqrt((playerX - nearX)**2 + (playerY - nearY)**2)
            
            if distance <= playerRadius:
                self.dispatch_event('on_collision')
                break

    def on_collision(self):
        pass

