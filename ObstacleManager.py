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
        self.topObstacleImageRed = pyglet.image.load("./assets/ArrowObstacleTopRed.png")
        self.topObstacleImageBlue = pyglet.image.load("./assets/ArrowObstacleTopBlue.png")
        self.topObstacleImageGreen = pyglet.image.load("./assets/ArrowObstacleTopGreen.png")
        self.topObstacleImageYellow = pyglet.image.load("./assets/ArrowObstacleTopYellow.png")
        self.bottomObstacleImageRed = pyglet.image.load("./assets/ArrowObstacleBottomRed.png")
        self.bottomObstacleImageBlue = pyglet.image.load("./assets/ArrowObstacleBottomBlue.png")
        self.bottomObstacleImageGreen = pyglet.image.load("./assets/ArrowObstacleBottomGreen.png")
        self.bottomObstacleImageYellow = pyglet.image.load("./assets/ArrowObstacleBottomYellow.png")

        self.run = False

        self.hardmode = False

    def draw(self):
        for obstacle in reversed(self.obstacles):
            obstacle.draw()
    
    def update(self, dt, hardMode):
        self.hardmode = hardMode
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
        
        difficultyLevel = level

        if self.hardmode:
            difficultyLevel = 4

        self.obstacleCenterRange = difficultyLevel - 1
        self.obstacleSpacing = (7 - difficultyLevel) * self.dim.unit
        self.difficultyLevel = difficultyLevel
        self.run = True


    def generate_obstacle(self):
        unit, w, h = self.dim.getDimensions()
        topImage = None
        bottomImage = None

        difficulty = self.difficultyLevel
        if self.hardmode:
            difficulty = 4

        if difficulty == 1:
            topImage = self.topObstacleImageBlue
            bottomImage = self.bottomObstacleImageBlue
            pass
        elif difficulty == 2:
            topImage = self.topObstacleImageGreen
            bottomImage = self.bottomObstacleImageGreen
            pass
        elif difficulty == 3:
            topImage = self.topObstacleImageYellow
            bottomImage = self.bottomObstacleImageYellow
            pass
        elif difficulty == 4: 
            topImage = self.topObstacleImageRed
            bottomImage = self.bottomObstacleImageRed
            pass

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
            topSprite = pyglet.sprite.Sprite(x=obstacleX, y=topObstacleY, img=topImage)
            topSprite.scale_y = obstacleHeight/topSprite.height
            topSprite.scale_x = obstacleWidth/topSprite.width

            #BOTTOM INIT AND SCALING 
            bottomSprite = pyglet.sprite.Sprite(x=obstacleX, y=bottomObstacleY, img=bottomImage)
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
    