from perlin_noise import PerlinNoise
from Obsticle import Obsticle
import random
import time

class ObsticleManager:
    def __init__(self, window):
        self.obsticles = []
        self.window = window
        self.obsticleSpeed = 100
        self.lastObsticleTime = time.time()
        self.noise = PerlinNoise()
        self.nextNoiseSeed = 1
        self.generate_boundaries()

    def generate_boundaries(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        boundarySize = 150

        bottomBoundaryY = bottom - boundarySize
        topBoundaryY = top

        topBoundary = Obsticle(-self.window.width/2, topBoundaryY, self.window.width, boundarySize, True)
        bottomBoundary = Obsticle(-self.window.width/2, bottomBoundaryY, self.window.width, boundarySize, True)

        self.obsticles.append(topBoundary)
        self.obsticles.append(bottomBoundary)
    
    def generate_obsticle(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        randomSegment = self.noise(self.nextNoiseSeed)*self.window.height/3#random.uniform(-self.window.height/3, self.window.height/3)
        self.nextNoiseSeed += 0.8
        obsticleSpacing = 150
        obsticleWidth = 200
        originX = self.window.width/2
              
        bottomObsticleY = bottom
        topObsticleY = randomSegment + obsticleSpacing
        topObsticleHeight = top - randomSegment - obsticleSpacing
        bottomObsticleHeight = randomSegment - obsticleSpacing - bottomObsticleY

        topObsticle = Obsticle(originX, topObsticleY, obsticleWidth, topObsticleHeight)
        bottomObsticle = Obsticle(originX, bottomObsticleY, obsticleWidth, bottomObsticleHeight)

        self.obsticles.append(topObsticle)
        self.obsticles.append(bottomObsticle)
        self.lastObsticleTime = time.time()

    def draw(self):
        for obsticle in self.obsticles:
            obsticle.draw()
    
    def update(self, dt):
        timeSinceLastObsticle = time.time() - self.lastObsticleTime
        for obsticle in self.obsticles:
            if not obsticle.boundary:
                obsticle.move(-self.obsticleSpeed*dt, 0)
                if obsticle.x + obsticle.width < -self.window.width/2:
                    self.obsticles.remove(obsticle)
            else:
                boundaryMoveSpeed = 5
                if obsticle.y > 0: # bottom
                    if obsticle.y > self.window.height/2 - 150:
                        obsticle.move(0, -boundaryMoveSpeed)
                else: # bottom
                    if obsticle.y < -self.window.height/2:
                        obsticle.move(0, boundaryMoveSpeed)

                    
        if timeSinceLastObsticle >= 5 or len(self.obsticles) == 0:
            self.generate_obsticle()
    
    def reset(self):
        self.obsticles = []
        self.generate_boundaries()

    