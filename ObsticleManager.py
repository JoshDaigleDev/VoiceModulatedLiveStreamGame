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
            obsticle.move(-self.obsticleSpeed*dt, 0)
            if obsticle.x + obsticle.width < -self.window.width/2:
                self.obsticles.remove(obsticle)
                
        if timeSinceLastObsticle >= 5 or len(self.obsticles) == 0:
            self.generate_obsticle()
    
    def reset(self):
        self.obsticles = []

    