from perlin_noise import PerlinNoise
from Obstacle import Obstacle
from LaserProjectile import LaserProjectile
import time

class ObstacleManager:
    def __init__(self, window):
        self.obstacles = []
        self.window = window
        self.obstacleSpeed = 300
        self.lastObstacleTime = time.time()
        self.noise = PerlinNoise()
        self.nextNoiseSeed = 1
        self.generate_boundaries()
        self.settingUp = True

    def generate_boundaries(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        boundarySize = 150

        bottomBoundaryY = bottom - boundarySize
        topBoundaryY = top

        topBoundary = Obstacle(-self.window.width/2, topBoundaryY, self.window.width, boundarySize, True)
        bottomBoundary = Obstacle(-self.window.width/2, bottomBoundaryY, self.window.width, boundarySize, True)

        topBoundary.passed = True
        bottomBoundary.passed = True

        self.obstacles.append(topBoundary)
        self.obstacles.append(bottomBoundary)
    
    def generate_obstacle(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        randomSegment = self.noise(self.nextNoiseSeed)*self.window.height/3#random.uniform(-self.window.height/3, self.window.height/3)
        self.nextNoiseSeed += 0.8
        obstacleSpacing = 150
        obstacleWidth = 200
        originX = self.window.width/2
              
        bottomObstacleY = bottom
        topObstacleY = randomSegment + obstacleSpacing
        topObstacleHeight = top - randomSegment - obstacleSpacing
        bottomObstacleHeight = randomSegment - obstacleSpacing - bottomObstacleY

        topObstacle = Obstacle(originX, topObstacleY, obstacleWidth, topObstacleHeight)
        bottomObstacle = Obstacle(originX, bottomObstacleY, obstacleWidth, bottomObstacleHeight)
        bottomObstacle.passed = True

        self.obstacles.append(topObstacle)
        self.obstacles.append(bottomObstacle)
        self.lastObstacleTime = time.time()

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()
    
    def update(self, dt):
        timeSinceLastObstacle = time.time() - self.lastObstacleTime
        for obstacle in self.obstacles:
            if not obstacle.boundary:
                obstacle.update(-self.obstacleSpeed * dt, 0)
                if obstacle.x + obstacle.width < -self.window.width/2:
                    self.obstacles.remove(obstacle)
            else:
                boundaryMoveSpeed = 5
                if obstacle.y > 0:
                    if obstacle.y > self.window.height/2 - 150:
                        obstacle.update(0, -boundaryMoveSpeed)
                    else: 
                        self.settingUp = False
                else: 
                    if obstacle.y < -self.window.height/2:
                        obstacle.update(0, boundaryMoveSpeed)

                    
        if timeSinceLastObstacle >= 2 or len(self.obstacles) == 0:
            self.generate_obstacle()
    
    def reset(self):
        self.settingUp = True
        self.obstacles = []
        self.generate_boundaries()

    