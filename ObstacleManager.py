import pyglet
from perlin_noise import PerlinNoise
from Obstacle import Obstacle
from LaserProjectile import LaserProjectile
import time

class ObstacleManager:
    def __init__(self, window):
        self.window = window
        self.obstacles = []
        self.obstacleSpeed = 300
        
        self.noise = PerlinNoise()
        self.obstacleSpacing = 200
        self.nextNoiseSeed = 1
        self.generate_boundaries()

        self.generationTime = 0
        self.generationTimeMax = 120
        self.topObstacleImage = pyglet.image.load("./assets/PixelPillar.png")
        self.bottomObstacleImage = pyglet.image.load("./assets/PixelPillar.png")

    def draw(self):
        for obstacle in reversed(self.obstacles):
            obstacle.draw()
    
    def update(self, dt):
        for obstacle in self.obstacles:
            if not obstacle.boundary:
                obstacle.update(-self.obstacleSpeed * dt, 0)
                if obstacle.x + obstacle.width < -self.window.width/2:
                    self.obstacles.remove(obstacle)
        

        self.generationTime += 1
        if len(self.obstacles) == 0 or self.generationTime >= self.generationTimeMax:
            self.generate_obstacle()
            self.generationTime = 0


    def generate_obstacle(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        randomSegment = self.noise(self.nextNoiseSeed) * self.window.height/3
        self.nextNoiseSeed += 0.8
        obstacleWidth = 300
        originX = self.window.width/2
              
        bottomObstacleY = bottom
        topObstacleY = randomSegment + self.obstacleSpacing
        topObstacleHeight = top - randomSegment - self.obstacleSpacing
        bottomObstacleHeight = randomSegment - self.obstacleSpacing - bottomObstacleY

        topSprite = None
        bottomSprite = None

        topSprite = pyglet.sprite.Sprite(x=originX, y=topObstacleY, img=self.topObstacleImage)
        topSprite.scale_y = topObstacleHeight/topSprite.height
        topSprite.scale_x = obstacleWidth/topSprite.width

        bottomSprite = pyglet.sprite.Sprite(x=originX, y=bottomObstacleY, img=self.bottomObstacleImage)
        bottomSprite.scale_y = bottomObstacleHeight/bottomSprite.height
        bottomSprite.scale_x = obstacleWidth/bottomSprite.width

        topObstacle = Obstacle(originX, topObstacleY, obstacleWidth, topObstacleHeight, sprite=topSprite, boundary=False)
        bottomObstacle = Obstacle(originX, bottomObstacleY, obstacleWidth, bottomObstacleHeight, sprite=bottomSprite, boundary=False)

        self.obstacles.append(topObstacle)
        self.obstacles.append(bottomObstacle)
        self.lastObstacleTime = time.time()

    
    def reset(self):
        self.obstacles = []
        self.generate_boundaries()
        

    def generate_boundaries(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        boundarySize = 175

        bottomBoundaryY = bottom 
        topBoundaryY = top - boundarySize

        topBoundary = Obstacle(-self.window.width/2, topBoundaryY, self.window.width, boundarySize, boundary=True)
        bottomBoundary = Obstacle(-self.window.width/2, bottomBoundaryY, self.window.width, boundarySize, boundary=True)

        topBoundary.passed = True
        bottomBoundary.passed = True

        self.obstacles.append(topBoundary)
        self.obstacles.append(bottomBoundary)
    