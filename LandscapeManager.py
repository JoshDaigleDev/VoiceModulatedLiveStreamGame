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
        grassSpeed = -1
        cloudSpeed = -0.1
        for element in self.grass:
            speedModifier = element[0]
            mover = element[1]
            mover.move(grassSpeed/speedModifier, 0)
            

            if mover.x + mover.sprite.image.width < -self.window.width/2:
                if speedModifier == 1:
                    rightMostGrass = self.grass[0][1]
                    for grass in self.grass:
                        grassSprite = grass[1]
                        if grass[0] == 1 and grassSprite.x > rightMostGrass.x:
                            rightMostGrass = grassSprite
                    mover.x = int(rightMostGrass.x + self.grass1Spacing)-1
                    print(mover.x)
                else:
                    mover.x = self.window.width/2
            mover.update()
        
        for element in self.clouds:
            self.nextNoiseSeed += 0.8
            speedModifier = element[0]
            copy = element[1] == 0
            cloud = element[2]
            cloud.move(cloudSpeed/speedModifier, self.noise(self.nextNoiseSeed)/10)
            cloud.update()
            if cloud.x + cloud.sprite.image.width < -self.window.width/2:
                self.clouds.remove(element)
            elif cloud.x < -self.window.width/2 and not copy:
                cloudSpriteCopy = pyglet.sprite.Sprite(x=self.window.width/2, y=cloud.y, img=cloud.sprite.image)
                cloudCopy = Mover(x=self.window.width/2, y=cloud.y, sprite=cloudSpriteCopy)
                self.clouds.append((speedModifier, 1, cloudCopy))
                newElement = (speedModifier, 0, cloud)
                self.clouds.remove(element)
                self.clouds.append(newElement)


    def draw(self):
        for atmosphereBit in self.atmosphere:
            atmosphereBit.draw()
  
        for element in self.clouds:
            mover = element[2]
            mover.draw()


        for element in self.grass:
            mover = element[1]
            mover.draw()


    def initCoords(self):
        self.grassY = -self.window.height/2 + self.boundarySize
        grass1Origin = -self.window.width/2
        self.grass1Spacing = self.grassR1C1Image.width

        self.grassR1C1X = grass1Origin
        self.grassR1C2X = grass1Origin + self.grass1Spacing
        self.grassR1C3X = grass1Origin + 2*self.grass1Spacing
        self.grassR1C4X = grass1Origin + 3*self.grass1Spacing
        self.grassR1C5X = grass1Origin + 4*self.grass1Spacing
        self.grassR1C6X = grass1Origin + 5*self.grass1Spacing

        self.grassR2C1X = -1.5*self.window.width/2
        self.grassR2C2X = -1.5*self.window.width/2 + self.grass2Image.width

        self.grassR3C1X = -self.window.width/3
        self.grassR3C2X = -self.window.width/3 + self.grass3Image.width

        self.grassR4C1X = -self.window.width/1.5
        self.grassR4C2X = -self.window.width/1.5 + self.grass4Image.width/1.75
        self.grassR4C3X = -self.window.width/1.5 + 2*self.grass4Image.width/1.75

        bigCloudSpacing = self.window.width/3
        bigCloudOrigin = -self.window.width/2

        self.cloud1X = bigCloudOrigin
        self.cloud1Y = self.window.height/8 

        self.cloud2X = bigCloudOrigin + bigCloudSpacing
        self.cloud2Y = self.window.height/8 

        self.cloud3X = bigCloudOrigin + 2*bigCloudSpacing
        self.cloud3Y = self.window.height/8 

        self.cloud4X = bigCloudOrigin + 3*bigCloudSpacing
        self.cloud4Y = self.window.height/8 

        self.midCloudSpacing = self.midCloud1Image.width
        midCloudOriginX = -self.window.width/2
        self.midCloudY = -self.window.height/24

        self.midCloud1X = midCloudOriginX
        self.midCloud2X = midCloudOriginX + self.midCloudSpacing
        self.midCloud3X = midCloudOriginX + 2*self.midCloudSpacing
        self.midCloud4X = midCloudOriginX + 3*self.midCloudSpacing

        self.atmosphereX = -self.window.width/2
        self.atmosphereY = -self.window.height/3
        self.atmosphereCorrection = 100

        self.atmosphereThickBottomY = -self.window.height/4 - self.atmosphereCorrection
        self.atmosphereThinBottomY = self.window.height/16 - self.atmosphereCorrection

        self.atmosphereThickTopY = -self.window.height/8 - self.atmosphereCorrection
        self.atmosphereThinTopY = self.window.height/6 - self.atmosphereCorrection


    def loadAssets(self):
        self.cloud1Image = pyglet.image.load("./assets/PixelCloud1.png")
        self.cloud2Image = pyglet.image.load("./assets/PixelCloud2.png")
        self.cloud3Image = pyglet.image.load("./assets/PixelCloud3.png")
        self.cloud4Image = pyglet.image.load("./assets/PixelCloud4.png")
        self.midCloud1Image = pyglet.image.load("./assets/PixelMidCloud1.png")
        self.midCloud2Image = pyglet.image.load("./assets/PixelMidCloud2.png")
        self.midCloud3Image = pyglet.image.load("./assets/PixelMidCloud3.png")
        self.midCloud4Image = pyglet.image.load("./assets/PixelMidCloud4.png")
        self.grassR1C1Image = pyglet.image.load("./assets/PixelGrass1.png")
        self.grassR1C2Image = pyglet.image.load("./assets/PixelGrass2.png")
        self.grassR1C3Image = pyglet.image.load("./assets/PixelGrass3.png")
        self.grassR1C4Image = pyglet.image.load("./assets/PixelGrass4.png")
        self.grassR1C5Image = pyglet.image.load("./assets/PixelGrass5.png")
        self.grassR1C6Image = pyglet.image.load("./assets/PixelGrass6.png")
        self.grass2Image = pyglet.image.load("./assets/Grass2.png")
        self.grass3Image = pyglet.image.load("./assets/Grass3.png")
        self.grass4Image = pyglet.image.load("./assets/Grass4.png")
        self.atmosphereImage = pyglet.image.load("./assets/Atmosphere.png")


    def initClouds(self):
        cloud1Sprite = pyglet.sprite.Sprite(img=self.cloud1Image, x=self.cloud1X, y=self.cloud1Y)
        cloud1 = Mover(self.cloud1X, self.cloud1Y, cloud1Sprite)
        self.clouds.append((1, 1, cloud1))
        
        cloud2Sprite = pyglet.sprite.Sprite(img=self.cloud2Image, x=self.cloud2X, y=self.cloud2Y)
        cloud2 = Mover(self.cloud2X, self.cloud2Y, cloud2Sprite)
        self.clouds.append((1, 1, cloud2))

        cloud3Sprite = pyglet.sprite.Sprite(img=self.cloud3Image, x=self.cloud3X, y=self.cloud3Y)
        cloud3 = Mover(self.cloud3X, self.cloud3Y, cloud3Sprite)
        self.clouds.append((1, 1, cloud3))

        cloud4Sprite = pyglet.sprite.Sprite(img=self.cloud4Image, x=self.cloud4X, y=self.cloud4Y)
        cloud4 = Mover(self.cloud4X, self.cloud4Y, cloud4Sprite)
        self.clouds.append((1, 1, cloud4))

        midCloud1Sprite = pyglet.sprite.Sprite(img=self.midCloud1Image, x=self.midCloud1X, y=self.midCloudY)
        midCloud1 = Mover(self.midCloud1X, self.midCloudY, midCloud1Sprite)
        self.clouds.append((2, 1, midCloud1))

        midCloud2Sprite = pyglet.sprite.Sprite(img=self.midCloud2Image, x=self.midCloud2X, y=self.midCloudY)
        midCloud2 = Mover(self.midCloud2X, self.midCloudY, midCloud2Sprite)
        self.clouds.append((2, 1, midCloud2))
        
        midCloud3Sprite = pyglet.sprite.Sprite(img=self.midCloud3Image, x=self.midCloud3X, y=self.midCloudY)
        midCloud3 = Mover(self.midCloud3X, self.midCloudY, midCloud3Sprite)
        self.clouds.append((2, 1, midCloud3))

        midCloud4Sprite = pyglet.sprite.Sprite(img=self.midCloud4Image, x=self.midCloud4X, y=self.midCloudY)
        midCloud4 = Mover(self.midCloud4X, self.midCloudY, midCloud4Sprite)
        self.clouds.append((2, 1, midCloud4))


    def initGrass(self):
        grassR1C1Sprite = pyglet.sprite.Sprite(img=self.grassR1C1Image, x=self.grassR1C1X, y=self.grassY)
        grassR1C1 = Mover(self.grassR1C1X, self.grassY, grassR1C1Sprite)

        grassR1C2Sprite = pyglet.sprite.Sprite(img=self.grassR1C2Image, x=self.grassR1C2X, y=self.grassY)
        grassR1C2 = Mover(self.grassR1C2X, self.grassY, grassR1C2Sprite)

        grassR1C3Sprite = pyglet.sprite.Sprite(img=self.grassR1C3Image, x=self.grassR1C3X, y=self.grassY)
        grassR1C3 = Mover(self.grassR1C3X, self.grassY, grassR1C3Sprite)

        grassR1C4Sprite = pyglet.sprite.Sprite(img=self.grassR1C4Image, x=self.grassR1C4X, y=self.grassY)
        grassR1C4 = Mover(self.grassR1C4X, self.grassY, grassR1C4Sprite)

        grassR1C5Sprite = pyglet.sprite.Sprite(img=self.grassR1C5Image, x=self.grassR1C5X, y=self.grassY)
        grassR1C5 = Mover(self.grassR1C5X, self.grassY, grassR1C5Sprite)

        grassR1C6Sprite = pyglet.sprite.Sprite(img=self.grassR1C6Image, x=self.grassR1C6X, y=self.grassY)
        grassR1C6 = Mover(self.grassR1C6X, self.grassY, grassR1C6Sprite)

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
        self.grass.append((1, grassR1C3))
        self.grass.append((1, grassR1C4))
        self.grass.append((1, grassR1C5))   
        self.grass.append((1, grassR1C6))   

    def initAtmosphere(self):
        #atmosphereThickBottom = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThickBottomY, width=self.window.width, height=300, color=(255,255,255, 50))
        #atmosphereThinBottom = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThinBottomY, width=self.window.width, height=20, color=(255,255,255, 50))
        #atmosphereThickTop = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThickTopY, width=self.window.width, height=300, color=(255,255,255, 50))
        #atmosphereThinTop = pyglet.shapes.Rectangle(x=self.atmosphereX, y=self.atmosphereThinTopY, width=self.window.width, height=20, color=(255,255,255, 50))
        #self.atmosphere.append(atmosphereThickBottom)
        #self.atmosphere.append(atmosphereThinBottom)
        #self.atmosphere.append(atmosphereThickTop)
        #self.atmosphere.append(atmosphereThinTop)

        atmosphere = pyglet.sprite.Sprite(img=self.atmosphereImage, x=self.atmosphereX, y=self.atmosphereY)
        self.atmosphere.append(atmosphere)

"""backgroundGrass = pyglet.image.load("./assets/Grass.png")
backgroundGrass2 = pyglet.image.load("./assets/Grass2.png")

bghSprite = pyglet.sprite.Sprite(img=backgroundGrass, x=0, y=-window.height/2 + 150)
bghSprite2 = pyglet.sprite.Sprite(img=backgroundGrass2, x=-window.width/2, y=-window.height/2 + 150)"""