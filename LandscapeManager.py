import pyglet
import random
from Mover import Mover
from perlin_noise import PerlinNoise
class LandscapeManager:

    def __init__(self, window):
        self.window = window
        self.grass = []
        self.clouds = []
        self.atmosphere = []
        self.boundarySize = 150
        self.noise = PerlinNoise()
        self.nextNoiseSeed = 1
        self.loadAssets()
        self.initCoords()
        self.initGrass()
        self.initClouds()
        self.initAtmosphere()


    def update(self):
        for element in self.grass:
            speed = element[0]
            mover = element[1]
            mover.move(-1/speed, 0)

            if mover.x + mover.sprite.image.width < -self.window.width/2:
                mover.x = self.window.width/2
            mover.update()
        
        for element in self.clouds:
            self.nextNoiseSeed += 0.8
            cloud = element[1]
            cloud.move(-0.2, self.noise(self.nextNoiseSeed)/10)
            cloud.update()
            if cloud.x + cloud.sprite.image.width < -self.window.width/2:
                self.clouds.remove(element)
            elif cloud.x < -self.window.width/2 and element[0] == 1:
                cloudSpriteCopy = pyglet.sprite.Sprite(x=self.window.width/2, y=cloud.y, img=cloud.sprite.image)
                cloudCopy = Mover(x=self.window.width/2, y=cloud.y, sprite=cloudSpriteCopy)
                self.clouds.append((1,cloudCopy))
                newElement = (0, cloud)
                self.clouds.remove(element)
                self.clouds.append(newElement)

        print(len(self.clouds))


    def draw(self):
        for atmosphereBit in self.atmosphere:
            atmosphereBit.draw()
  
        for element in self.clouds:
            mover = element[1]
            mover.draw()


        for element in self.grass:
            mover = element[1]
            mover.draw()


    def initCoords(self):
        self.grassY = -self.window.height/2 + self.boundarySize

        self.grassR1C1X = 0
        self.grassR1C2X = self.grass1Image.width

        self.grassR2C1X = -1.5*self.window.width/2
        self.grassR2C2X = -1.5*self.window.width/2 + self.grass2Image.width

        self.grassR3C1X = -self.window.width/3
        self.grassR3C2X = -self.window.width/3 + self.grass3Image.width

        self.grassR4C1X = -self.window.width/1.5
        self.grassR4C2X = -self.window.width/1.5 + self.grass4Image.width/1.75
        self.grassR4C3X = -self.window.width/1.5 + 2*self.grass4Image.width/1.75

        self.cloud1X = -self.window.width/2
        self.cloud1Y = -self.window.height/12 

        self.cloud2X = -self.window.width/4
        self.cloud2Y = self.window.height/12 

        self.cloud3X = 0
        self.cloud3Y = -self.window.height/12       

        self.cloud4X = self.window.width/4 
        self.cloud4Y = self.window.height/12

        self.atmosphereX = -self.window.width/2
        self.atmosphereCorrection = 100

        self.atmosphereThickBottomY = -self.window.height/4 - self.atmosphereCorrection
        self.atmosphereThinBottomY = self.window.height/16 - self.atmosphereCorrection

        self.atmosphereThickTopY = -self.window.height/8 - self.atmosphereCorrection
        self.atmosphereThinTopY = self.window.height/6 - self.atmosphereCorrection


    def loadAssets(self):
        self.cloud1Image = pyglet.image.load("./assets/Cloud1.png")
        self.cloud2Image = pyglet.image.load("./assets/Cloud2.png")
        self.cloud3Image = pyglet.image.load("./assets/Cloud3.png")
        self.cloud4Image = pyglet.image.load("./assets/Cloud4.png")
        self.grass1Image = pyglet.image.load("./assets/Grass1.png")
        self.grass2Image = pyglet.image.load("./assets/Grass2.png")
        self.grass3Image = pyglet.image.load("./assets/Grass3.png")
        self.grass4Image = pyglet.image.load("./assets/Grass4.png")


    def initClouds(self):
        cloud1Sprite = pyglet.sprite.Sprite(img=self.cloud1Image, x=self.cloud1X, y=self.cloud1Y)
        cloud1 = Mover(self.cloud1X, self.cloud1Y, cloud1Sprite)
        self.clouds.append((1,cloud1))
        
        cloud2Sprite = pyglet.sprite.Sprite(img=self.cloud2Image, x=self.cloud2X, y=self.cloud2Y)
        cloud2 = Mover(self.cloud2X, self.cloud2Y, cloud2Sprite)
        self.clouds.append((1,cloud2))

        cloud3Sprite = pyglet.sprite.Sprite(img=self.cloud3Image, x=self.cloud3X, y=self.cloud3Y)
        cloud3 = Mover(self.cloud3X, self.cloud3Y, cloud3Sprite)
        self.clouds.append((1,cloud3))

        cloud4Sprite = pyglet.sprite.Sprite(img=self.cloud4Image, x=self.cloud4X, y=self.cloud4Y)
        cloud4 = Mover(self.cloud4X, self.cloud4Y, cloud4Sprite)
        self.clouds.append((1,cloud4))


    def initGrass(self):
        grassR1C1Sprite = pyglet.sprite.Sprite(img=self.grass1Image, x=self.grassR1C1X, y=self.grassY)
        grassR1C1 = Mover(self.grassR1C1X, self.grassY, grassR1C1Sprite)

        grassR1C2Sprite = pyglet.sprite.Sprite(img=self.grass1Image, x=self.grassR1C2X, y=self.grassY)
        grassR1C2 = Mover(self.grassR1C2X, self.grassY, grassR1C2Sprite)


        grassR2C1Sprite = pyglet.sprite.Sprite(img=self.grass2Image, x=self.grassR2C1X, y=self.grassY)
        grassR2C1 = Mover(self.grassR2C1X, self.grassY, grassR2C1Sprite)

        grassR2C2Sprite = pyglet.sprite.Sprite(img=self.grass2Image, x=self.grassR2C2X, y=self.grassY)
        grassR2C2 = Mover(self.grassR2C2X, self.grassY, grassR2C2Sprite)


        grassR3C1Sprite = pyglet.sprite.Sprite(img=self.grass3Image, x=self.grassR3C1X, y=self.grassY)
        grassR3C1 = Mover(self.grassR3C1X, self.grassY, grassR3C1Sprite)

        grassR3C2Sprite = pyglet.sprite.Sprite(img=self.grass3Image, x=self.grassR3C2X, y=self.grassY)
        grassR3C2 = Mover(self.grassR3C2X, self.grassY, grassR3C2Sprite)

        
        grassR4C1Sprite = pyglet.sprite.Sprite(img=self.grass4Image, x=self.grassR4C1X, y=self.grassY + self.window.height/128)
        grassR4C1 = Mover(self.grassR4C1X, self.grassY + self.window.height/128, grassR4C1Sprite)

        grassR4C2Sprite = pyglet.sprite.Sprite(img=self.grass4Image, x=self.grassR4C2X, y=self.grassY + self.window.height/128)
        grassR4C2 = Mover(self.grassR4C2X, self.grassY + self.window.height/128, grassR4C2Sprite)

        grassR4C3Sprite = pyglet.sprite.Sprite(img=self.grass4Image, x=self.grassR4C3X, y=self.grassY + self.window.height/128)
        grassR4C3 = Mover(self.grassR4C3X, self.grassY + self.window.height/128, grassR4C3Sprite)

        self.grass.append((4, grassR4C1))
        self.grass.append((4, grassR4C2))
        self.grass.append((4, grassR4C3))

        self.grass.append((3, grassR3C1))
        self.grass.append((3, grassR3C2))

        self.grass.append((2, grassR2C1))
        self.grass.append((2, grassR2C2))

        self.grass.append((1, grassR1C1))
        self.grass.append((1, grassR1C2))


    def initAtmosphere(self):
        atmosphereThickBottom = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThickBottomY, width=self.window.width, height=300, color=(255,255,255, 50))
        atmosphereThinBottom = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThinBottomY, width=self.window.width, height=20, color=(255,255,255, 50))
        atmosphereThickTop = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThickTopY, width=self.window.width, height=300, color=(255,255,255, 50))
        atmosphereThinTop = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThinTopY, width=self.window.width, height=20, color=(255,255,255, 50))

        self.atmosphere.append(atmosphereThickBottom)
        self.atmosphere.append(atmosphereThinBottom)
        self.atmosphere.append(atmosphereThickTop)
        self.atmosphere.append(atmosphereThinTop)

"""backgroundGrass = pyglet.image.load("./assets/Grass.png")
backgroundGrass2 = pyglet.image.load("./assets/Grass2.png")

bghSprite = pyglet.sprite.Sprite(img=backgroundGrass, x=0, y=-window.height/2 + 150)
bghSprite2 = pyglet.sprite.Sprite(img=backgroundGrass2, x=-window.width/2, y=-window.height/2 + 150)"""