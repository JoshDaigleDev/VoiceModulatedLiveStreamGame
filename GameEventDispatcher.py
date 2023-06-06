import pyglet
import math

class GameEventDispatcher(pyglet.event.EventDispatcher):
    def __init__(self, gameManager):
        self.obstacleManager = gameManager.obstacleManager
        self.playerManager = gameManager.playerManager
        self.particleSystemManager = gameManager.particleSystemManager
        self.window = gameManager.window
    
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

    def doParticlePhysics(self, dt):
        damping_factor = 0.8  # Adjust the damping factor as needed
        airDrag = 0.98
        groundFriction = 0.98
        gravity = 0.98
        splatter = False
        if not splatter:
            dt = 1

        for system in self.particleSystemManager.particleSystems:
            if system.externalForce:
                for particle in system.particles:
                    particle.yVelocity -= gravity
                    particle.xVelocity *= airDrag
                    particle.yVelocity *= airDrag
                    for obstacle in self.obstacleManager.obstacles:
                        if obstacle.contains(particle.x, particle.y, particle.radius):
                            topObstacle = False
                            if obstacle.top == self.window.height / 2:
                                topObstacle = True

                            nextX = particle.x + particle.xVelocity
                            nextY = particle.y + particle.yVelocity

                            withinX = nextX >= obstacle.left and nextX < obstacle.right

                            if not obstacle.boundary:
                                if withinX:
                                    newVelocity = -(particle.xVelocity * damping_factor)*dt
                                    if abs(newVelocity) < 2:
                                        newVelocity = 0
                                    particle.xVelocity = newVelocity 
                            if topObstacle:
                                if nextY + particle.radius >= obstacle.bottom:   
                                    newVelocity = -(particle.yVelocity * damping_factor)*dt
                                    if abs(newVelocity) < 4:
                                        newVelocity = 0
                                    particle.yVelocity = newVelocity
                            else:          
                                if nextY - particle.radius <= obstacle.top:  
                                    newVelocity = -(particle.yVelocity * damping_factor)*dt
                                    if abs(newVelocity) < 4:
                                        newVelocity = 0
                                    particle.yVelocity = newVelocity 
                                
                                if not topObstacle:
                                    if particle.y + particle.radius >= obstacle.top:
                                        particle.xVelocity *= groundFriction
                                

    def on_score(self):
        pass  


    def on_collision(self):
        pass
