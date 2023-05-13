from obsticle import Obsticle
import random
import time
class obsticle_coordinator:
    def __init__(self, window):
        self.obsticles = []
        self.window = window
        self.generate_obsticle()
        self.obsticleSpeed = 100
        self.lastObsticleTime = time.time()
    
    def generate_obsticle(self):
        top = self.window.height/2
        bottom = -self.window.height/2
        randomSegment = random.uniform(-self.window.height/3, self.window.height/3)
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
            if obsticle.x + obsticle.width/2 < -self.window.width/2:
                self.obsticles.remove(obsticle)
        print(timeSinceLastObsticle)
        if timeSinceLastObsticle >= 5:
            self.generate_obsticle()
    
                


    