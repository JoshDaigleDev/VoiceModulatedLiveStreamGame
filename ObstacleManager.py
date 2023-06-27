import pyglet
from Obstacle import Obstacle
import random

class ObstacleManager:
    def __init__(self, dim):
        self.dim = dim
        self.obstacles = []
        self.obstacleSpeed = 300
        
        self.generate_boundaries()

        self.generationTime = 0
        self.generationTimeMax = 150
        self.topObstacleImage = pyglet.image.load("./assets/ArrowObstacleTop.png")
        self.bottomObstacleImage = pyglet.image.load("./assets/ArrowObstacle.png")

        self.run = False

    def draw(self):
        for obstacle in reversed(self.obstacles):
            obstacle.draw()
    
    def update(self, dt):
        if self.run: 
            for obstacle in self.obstacles:
                if not obstacle.boundary:
                    obstacle.update(-self.obstacleSpeed * dt, 0)
                    if obstacle.x + obstacle.width < -self.dim.w:
                        self.obstacles.remove(obstacle)
            
            self.generationTime += 1
            if len(self.obstacles) == 0 or self.generationTime >= self.generationTimeMax:
                self.generate_obstacle()
                self.generationTime = 0
    

    def setDifficulty(self, level):
        self.obstacleCenterRange = level - 1
        self.obstacleSpacing = (7 - level) * self.dim.unit
        self.run = True


    def generate_obstacle(self):
        unit, w, h = self.dim.getDimensions()

        #COORDINATES 
        try:
            obstacleSetCenter = random.randint(-self.obstacleCenterRange, self.obstacleCenterRange)*unit
            obstacleWidth = 6*unit
            obstacleHeight = 7*unit
            obstacleX = w       
            topObstacleY = obstacleSetCenter + self.obstacleSpacing
            bottomObstacleY = obstacleSetCenter - self.obstacleSpacing - obstacleHeight


            #SPRITES 
            topSprite = None
            bottomSprite = None

            #TOP INIT AND SCALING 
            topSprite = pyglet.sprite.Sprite(x=obstacleX, y=topObstacleY, img=self.topObstacleImage)
            topSprite.scale_y = obstacleHeight/topSprite.height
            topSprite.scale_x = obstacleWidth/topSprite.width

            #BOTTOM INIT AND SCALING 
            bottomSprite = pyglet.sprite.Sprite(x=obstacleX, y=bottomObstacleY, img=self.bottomObstacleImage)
            bottomSprite.scale_y = obstacleHeight/bottomSprite.height
            bottomSprite.scale_x = obstacleWidth/bottomSprite.width

            #OBSTACLE OBJECTS 
            topObstacle = Obstacle(obstacleX, topObstacleY, obstacleWidth, obstacleHeight, top=True, sprite=topSprite, boundary=False)
            bottomObstacle = Obstacle(obstacleX, bottomObstacleY, obstacleWidth, obstacleHeight, sprite=bottomSprite, boundary=False)

            self.obstacles.append(topObstacle)
            self.obstacles.append(bottomObstacle)
        except ValueError:
            print(self.obstacleCenterRange)

    
    def reset(self):
        self.obstacles = []
        self.generate_boundaries()
        self.run = False
        

    def generate_boundaries(self):
        top = self.dim.h
        bottom = -self.dim.h
        boundarySize = 3*self.dim.unit

        bottomBoundaryY = bottom 
        topBoundaryY = top - boundarySize

        topBoundary = Obstacle(-self.dim.w, topBoundaryY, 2 * self.dim.w, boundarySize, top=True, boundary=True)
        bottomBoundary = Obstacle(-self.dim.w, bottomBoundaryY, 2 * self.dim.w, boundarySize, boundary=True)

        topBoundary.passed = True
        bottomBoundary.passed = True

        self.obstacles.append(topBoundary)
        self.obstacles.append(bottomBoundary)
    