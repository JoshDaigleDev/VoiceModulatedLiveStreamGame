import pyglet
import math

class GameEventDispatcher(pyglet.event.EventDispatcher):
    def __init__(self, game):
        self.obstacleManager = game.obstacleManager
        self.playerManager = game.playerManager
        self.particleSystemManager = game.particleSystemManager    
    
    def detectCollision(self):
        playerX = self.playerManager.player.x
        playerY = self.playerManager.player.y
        playerRadius = self.playerManager.player.radius
        buffer = 10

        for obstacle in self.obstacleManager.obstacles:
            nearX = max(obstacle.left, min(playerX, obstacle.right))
            nearY = max(obstacle.bottom, min(playerY, obstacle.top))

            distance = math.sqrt((playerX - nearX)**2 + (playerY - nearY)**2)
            
            if distance <= playerRadius-buffer:
                self.dispatch_event('on_collision')
                break
    

    def detectScore(self):
        playerX = self.playerManager.player.x
        for obstacle in self.obstacleManager.obstacles:
            if not obstacle.passed:
                if playerX >= obstacle.x:
                    obstacle.passed = True
                    self.dispatch_event('on_score')


    def on_score(self):
        pass  


    def on_collision(self):
        pass
