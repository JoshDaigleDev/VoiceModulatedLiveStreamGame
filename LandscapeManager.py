import pyglet
from LandscapeMoverGroup import LandscapeMoverGroup
class LandscapeManager:

    def __init__(self, window):
        self.window = window
        self.boundarySize = 150

        self.initAtmosphere()
        
        self.initFirstGrass()
        self.initSecondGrass()
        self.initThirdGrass()
        self.initFourthGrass()

        self.initTopClouds()
        self.initMidClouds()
        self.initBotClouds()


    def update(self):
        self.firstGrass.update()
        self.secondGrass.update()
        self.thirdGrass.update()
        self.fourthGrass.update()

        self.topClouds.update()
        self.midClouds.update()
        self.botClouds.update()

    
    def draw(self):
        self.atmosphere.draw()

        self.fourthGrass.draw()
        self.thirdGrass.draw()
        self.secondGrass.draw()
        self.firstGrass.draw()

        self.botClouds.draw()
        self.midClouds.draw()
        self.topClouds.draw()


    def initAtmosphere(self):
        atmosphereImage = pyglet.image.load("./assets/Atmosphere.png")
        atmosphereX = -self.window.width/2
        atmosphereY = -self.window.height/3
        self.atmosphere = pyglet.sprite.Sprite(img=atmosphereImage, x=atmosphereX, y=atmosphereY)

    def initTopClouds(self):
        self.topCloudSpacing = 620
        self.topCloudSpeed = 0.4
        self.topCloudX = -self.window.width/2
        self.topCloudY = self.window.height/8 
        self.topClouds = LandscapeMoverGroup(self.window, self.topCloudSpacing, self.topCloudSpeed, self.topCloudX, self.topCloudY)

        self.topClouds.addMover("./assets/PixelCloud1.png")
        self.topClouds.addMover("./assets/PixelCloud2.png")
        self.topClouds.addMover("./assets/PixelCloud3.png")
        self.topClouds.addMover("./assets/PixelCloud4.png")
        self.topClouds.addMover("./assets/PixelCloud1.png")
        self.topClouds.addMover("./assets/PixelCloud2.png")
        self.topClouds.addMover("./assets/PixelCloud3.png")
        self.topClouds.addMover("./assets/PixelCloud4.png")


    def initMidClouds(self):
        self.midCloudSpacing = 512
        self.midCloudSpeed = 0.3
        self.midCloudX = -self.window.width/2
        self.midCloudY = 0
        self.midClouds = LandscapeMoverGroup(self.window, self.midCloudSpacing, self.midCloudSpeed, self.midCloudX, self.midCloudY)

        self.midClouds.addMover("./assets/PixelMidCloud1.png")
        self.midClouds.addMover("./assets/PixelMidCloud2.png")
        self.midClouds.addMover("./assets/PixelMidCloud3.png")
        self.midClouds.addMover("./assets/PixelMidCloud4.png")
        self.midClouds.addMover("./assets/PixelMidCloud1.png")


    def initBotClouds(self):
        self.botCloudSpacing = 320
        self.botCloudSpeed = 0.2
        self.botCloudX = -self.window.width/2
        self.botCloudY = -self.window.height/8 
        self.botClouds = LandscapeMoverGroup(self.window, self.botCloudSpacing, self.botCloudSpeed, self.botCloudX, self.botCloudY)

        self.botClouds.addMover("./assets/PixelSmallCloud1.png")
        self.botClouds.addMover("./assets/PixelSmallCloud2.png")
        self.botClouds.addMover("./assets/PixelSmallCloud3.png")
        self.botClouds.addMover("./assets/PixelSmallCloud4.png")
        self.botClouds.addMover("./assets/PixelSmallCloud1.png")
        self.botClouds.addMover("./assets/PixelSmallCloud2.png")
        self.botClouds.addMover("./assets/PixelSmallCloud3.png")
        self.botClouds.addMover("./assets/PixelSmallCloud4.png") 

    def initFirstGrass(self):
        self.firstGrassWidth = 512
        self.firstGrassSpeed = 1
        self.firstGrassX = -self.window.width/2
        self.firstGrassY = -self.window.height/2 + self.boundarySize
        self.firstGrass = LandscapeMoverGroup(self.window, self.firstGrassWidth, self.firstGrassSpeed, self.firstGrassX, self.firstGrassY)
        
        self.firstGrass.addMover("./assets/PixelGrass1.png")
        self.firstGrass.addMover("./assets/PixelGrass2.png")
        self.firstGrass.addMover("./assets/PixelGrass3.png")
        self.firstGrass.addMover("./assets/PixelGrass4.png")
        self.firstGrass.addMover("./assets/PixelGrass5.png")
        self.firstGrass.addMover("./assets/PixelGrass6.png")
    

    def initSecondGrass(self):
        self.secondGrassWidth = 2048
        self.secondGrassSpeed = 0.7
        self.secondGrassX = -self.window.width/2
        self.secondGrassY = -self.window.height/2 + self.boundarySize
        self.secondGrass = LandscapeMoverGroup(self.window, self.secondGrassWidth, self.secondGrassSpeed, self.secondGrassX, self.secondGrassY)
        
        self.secondGrass.addMover("./assets/Grass2.png")
        self.secondGrass.addMover("./assets/Grass2.png")


    def initThirdGrass(self):
        self.thirdGrassWidth = 2048
        self.thirdGrassSpeed = 0.4
        self.thirdGrassX = -self.window.width/3
        self.thirdGrassY = -self.window.height/2 + self.boundarySize
        self.thirdGrass = LandscapeMoverGroup(self.window, self.thirdGrassWidth, self.thirdGrassSpeed, self.thirdGrassX, self.thirdGrassY)
        
        self.thirdGrass.addMover("./assets/Grass3.png")
        self.thirdGrass.addMover("./assets/Grass3.png")


    def initFourthGrass(self):
        self.fourthGrassWidth = 2048
        self.fourthGrassSpeed = 0.1
        self.fourthGrassX = -self.window.width
        self.fourthGrassY = -self.window.height/2 + self.boundarySize
        self.fourthGrass = LandscapeMoverGroup(self.window, self.fourthGrassWidth, self.fourthGrassSpeed, self.fourthGrassX, self.fourthGrassY)
        
        self.fourthGrass.addMover("./assets/Grass4.png")
        self.fourthGrass.addMover("./assets/Grass4.png")
