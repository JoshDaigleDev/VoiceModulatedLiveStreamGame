import pyglet
from LandscapeMoverGroup import LandscapeMoverGroup
class LandscapeManager:

    def __init__(self, dim, rendering):
        self.dim = dim
        self.batch = rendering[0]
        self.ordering = rendering[1]
        self.boundarySize = 3 * dim.unit
        self.init(dim)

    def update(self):
        self.firstGrass.update()
        self.secondGrass.update()
        self.thirdGrass.update()
        self.fourthGrass.update()

        self.topClouds.update()
        self.midClouds.update()
        self.botClouds.update()

    def updateClouds(self, modifier=1):
        self.topClouds.update(modifier)
        self.midClouds.update(modifier)
        self.botClouds.update(modifier)

    def init(self, dim):
        unit, w, h = dim.getDimensions()

        self.initAtmosphere(unit, w)

        #Clouds
        self.initTopClouds(unit, w)
        self.initMidClouds(unit, w)
        self.initBotClouds(unit, w)

        #Grass
        self.initFirstGrass(unit, w)
        self.initSecondGrass(unit, w)
        self.initThirdGrass(unit)
        self.initFourthGrass(unit, w)


    def initAtmosphere(self, unit, w):
        atmosphereImage = pyglet.image.load("./assets/Atmosphere.png")
        atmosphereX = -w
        atmosphereY = -7*unit

        self.atmosphere = pyglet.sprite.Sprite(img=atmosphereImage, x=atmosphereX, y=atmosphereY, batch=self.batch, group=self.ordering[0])

    def initTopClouds(self, unit, w):
        topCloudSpacing = 620
        topCloudSpeed = 0.4
        topCloudX = -w
        topCloudY = 2*unit
        
        self.topClouds = LandscapeMoverGroup(self.dim, self.batch, self.ordering[3], topCloudSpacing, topCloudSpeed, topCloudX, topCloudY)
        self.topClouds.addMover("./assets/PixelCloud1.png")
        self.topClouds.addMover("./assets/PixelCloud2.png")
        self.topClouds.addMover("./assets/PixelCloud3.png")
        self.topClouds.addMover("./assets/PixelCloud4.png")
        self.topClouds.addMover("./assets/PixelCloud1.png")
        self.topClouds.addMover("./assets/PixelCloud2.png")
        self.topClouds.addMover("./assets/PixelCloud3.png")
        self.topClouds.addMover("./assets/PixelCloud4.png")


    def initMidClouds(self, unit, w):
        midCloudSpacing = 512
        midCloudSpeed = 0.3
        midCloudX = -w
        midCloudY = -unit

        self.midClouds = LandscapeMoverGroup(self.dim, self.batch, self.ordering[2], midCloudSpacing, midCloudSpeed, midCloudX, midCloudY)
        self.midClouds.addMover("./assets/PixelMidCloud1.png")
        self.midClouds.addMover("./assets/PixelMidCloud2.png")
        self.midClouds.addMover("./assets/PixelMidCloud3.png")
        self.midClouds.addMover("./assets/PixelMidCloud4.png")
        self.midClouds.addMover("./assets/PixelMidCloud1.png")


    def initBotClouds(self, unit, w):
        botCloudSpacing = 320
        botCloudSpeed = 0.2
        botCloudX = -w
        botCloudY = -2.5*unit

        self.botClouds = LandscapeMoverGroup(self.dim, self.batch, self.ordering[1], botCloudSpacing, botCloudSpeed, botCloudX, botCloudY)
        self.botClouds.addMover("./assets/PixelSmallCloud1.png")
        self.botClouds.addMover("./assets/PixelSmallCloud2.png")
        self.botClouds.addMover("./assets/PixelSmallCloud3.png")
        self.botClouds.addMover("./assets/PixelSmallCloud4.png")
        self.botClouds.addMover("./assets/PixelSmallCloud1.png")
        self.botClouds.addMover("./assets/PixelSmallCloud2.png")
        self.botClouds.addMover("./assets/PixelSmallCloud3.png")
        self.botClouds.addMover("./assets/PixelSmallCloud4.png") 

    def initFirstGrass(self, unit, w):
        firstGrassWidth = 512
        firstGrassSpeed = 1
        firstGrassX = -w
        firstGrassY = -7*unit

        self.firstGrass = LandscapeMoverGroup(self.dim, self.batch, self.ordering[5], firstGrassWidth, firstGrassSpeed, firstGrassX, firstGrassY)
        self.firstGrass.addMover("./assets/PixelGrass1.png")
        self.firstGrass.addMover("./assets/PixelGrass2.png")
        self.firstGrass.addMover("./assets/PixelGrass3.png")
        self.firstGrass.addMover("./assets/PixelGrass4.png")
        self.firstGrass.addMover("./assets/PixelGrass5.png")
        self.firstGrass.addMover("./assets/PixelGrass6.png")
    

    def initSecondGrass(self, unit, w):
        secondGrassWidth = 2048
        secondGrassSpeed = 0.7
        secondGrassX = -w
        secondGrassY = -7*unit

        self.secondGrass = LandscapeMoverGroup(self.dim, self.batch, self.ordering[4], secondGrassWidth, secondGrassSpeed, secondGrassX, secondGrassY)
        self.secondGrass.addMover("./assets/Grass2.png")
        self.secondGrass.addMover("./assets/Grass2.png")


    def initThirdGrass(self, unit):
        thirdGrassWidth = 2048
        thirdGrassSpeed = 0.4
        thirdGrassX = -4*unit
        thirdGrassY = -7*unit

        self.thirdGrass = LandscapeMoverGroup(self.dim, self.batch, self.ordering[3], thirdGrassWidth, thirdGrassSpeed, thirdGrassX, thirdGrassY)
        self.thirdGrass.addMover("./assets/Grass3.png")
        self.thirdGrass.addMover("./assets/Grass3.png")


    def initFourthGrass(self, unit, w):
        fourthGrassWidth = 2048
        fourthGrassSpeed = 0.1
        fourthGrassX = -2*w
        fourthGrassY = -7*unit

        self.fourthGrass = LandscapeMoverGroup(self.dim, self.batch, self.ordering[2], fourthGrassWidth, fourthGrassSpeed, fourthGrassX, fourthGrassY)
        self.fourthGrass.addMover("./assets/Grass4.png")
        self.fourthGrass.addMover("./assets/Grass4.png")
