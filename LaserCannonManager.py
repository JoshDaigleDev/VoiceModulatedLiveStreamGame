import pyglet
import math
from LaserProjectile import LaserProjectile
class LaserCannonManager:

    def __init__(self, window, playerManager, particleSystemManager):
        self.window = window
        self.playerManager = playerManager
        self.particleSystemManager = particleSystemManager
        self.barrelBaseX = -self.window.width/2 + self.window.width/12
        self.barrelBaseY = self.window.height/4
        self.laserWidth = 200
        self.load_assets()
        self.init_sprites()
        self.charging = False
        self.chargeTime = 0
        self.maxCharge = 60
        self.fired = False
        self.anchorX = -self.window.width/2 + 100
        self.anchorY = self.window.height/2

    def update(self):
        if self.charging:
            self.chargeTime += 1
            if self.chargeTime == self.maxCharge:
                self.fire_laser()
                self.chargeTime = 0
                self.charging = False

        #self.laserBarrelSprite.rotation = self.getAngleToPlayer()
        #elf.laserCharge.rotation = self.getAngleToPlayer()
        self.laserCharge.width = self.laserWidth * (self.chargeTime / self.maxCharge)

    
    def getAngleToPlayer(self):

        diffX = self.playerManager.player.x - self.laserBarrelSprite.x
        diffY = self.playerManager.player.y - self.laserBarrelSprite.y
        return -math.degrees(math.atan2(diffY, diffX))
    
    def draw(self):
        self.laserCharge.draw()
        self.laserBarrelSprite.draw()
        circle = pyglet.shapes.Circle(self.laserBarrelSprite.x, self.laserBarrelSprite.y, 25, color=(0, 255, 0, 100))
        circle.draw()





    #def draw_laser_cannon(self):



    def load_assets(self):
        self.laserBarrelImage = pyglet.image.load("./assets/LaserBarrel.png")
        self.laserBarrelImage.anchor_x = self.laserBarrelImage.width // 6 
        self.laserBarrelImage.anchor_y = self.laserBarrelImage.height // 2

    def init_sprites(self):
        self.laserBarrelSprite = pyglet.sprite.Sprite(img=self.laserBarrelImage, x=self.barrelBaseX, y=self.barrelBaseY)
        self.laserBarrelSprite.scale = self.laserWidth / self.laserBarrelSprite.width
        self.laserCharge = pyglet.shapes.Rectangle(x=self.barrelBaseX, y=self.barrelBaseY, width=self.laserWidth, height=self.laserWidth/8, color=(255,0,0))
        self.laserCharge.anchor_x = self.laserWidth // 6 
        self.laserCharge.anchor_y = self.laserWidth // 8


    def start_laser(self):
        self.charging = True
    
    def fire_laser(self):
        laser = LaserProjectile(self.laserBarrelSprite.x, self.laserBarrelSprite.y, self.laserWidth*10, self.laserWidth/8, self.getAngleToPlayer())
        self.particleSystemManager.fire_laser(laser)
        self.fired = True

    def reset(self):
        self.fired = False
