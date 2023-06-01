import pyglet
import math
from LaserProjectile import LaserProjectile
class LaserCannonManager:

    def __init__(self, window, playerManager, particleSystemManager):
        self.window = window
        self.playerManager = playerManager
        self.particleSystemManager = particleSystemManager
        self.anchorX = int(-self.window.width/2 + self.window.width/16)
        self.anchorY = int(self.window.height/8)
        self.scaleUnit = self.window.width/200
        #self.laserBaseWidth = self.laserWidth*2/3
        self.charging = False
        self.chargeTime = 0
        self.postChargeTime = 0
        self.postChargeMax = 8
        self.maxCharge = 64
        self.postChargeTimeIncrement = 1
        self.fired = False
        self.reverseCharge = False
        self.postCharging = False
        self.load_assets()
        self.init_sprites()



    def update(self):
        if self.charging:
            self.chargeTime += 1
            if self.chargeTime == self.maxCharge and not self.postCharging:
                self.fire_laser()
                self.charging = False
                self.chargeTime = 0
                self.postCharging = True
        if self.postCharging:
            if self.reverseCharge:
                self.postChargeTimeIncrement = -1
                if self.postChargeTime <= 0:
                    self.postCharging = False
                    self.reverseCharge = False 
    
                else:
                    self.postChargeTime += self.postChargeTimeIncrement
            else:
                self.postChargeTimeIncrement = 1
                if self.postChargeTime >= self.postChargeMax:
                    self.reverseCharge = True
                else:
                    self.postChargeTime += self.postChargeTimeIncrement


        self.laserCharge.width = self.laserWidth * (self.chargeTime / self.maxCharge)
        self.laserBarrelSprite.scale_x = 1-0.005*self.postChargeTime
        if not self.postCharging:
            self.laserBarrelSprite.scale_y = 1+0.001*self.chargeTime
        else: 
            if not self.reverseCharge:
                self.laserBarrelSprite.scale_y = 1+0.001*self.maxCharge - 0.008*self.postChargeTime
            else: 
                self.laserBarrelSprite.scale_y = 1

        
        self.trim_sound()


        self.laserBarrelSprite.rotation = self.getAngleToPlayer()
        self.laserBaseSprite.rotation = self.getAngleToPlayer()
        self.laserCharge.rotation = self.getAngleToPlayer()

    
    def getAngleToPlayer(self):

        diffX = self.playerManager.player.x - self.laserBarrelSprite.x
        diffY = self.playerManager.player.y - self.laserBarrelSprite.y
        return -math.degrees(math.atan2(diffY, diffX))
    
    def draw(self):
        self.draw_laser_cannon()
        if False:
            circle = pyglet.shapes.Circle(self.anchorX, self.anchorY, 25, color=(0, 255, 0, 100))
            circle.draw()
            line = pyglet.shapes.Line(x=self.anchorX, y=self.anchorY, x2=0, y2=0, width=12, color=(100,255,100, 100))
            line.draw()



    def draw_laser_cannon(self):
        self.laserPlatformSprite.draw()
        self.laserCharge.draw()
        self.laserBarrelSprite.draw()
        self.laserBaseSprite.draw()

    def load_assets(self):
        self.laserBarrelImage = pyglet.image.load("./assets/PixelBarrel.png")
        self.laserBarrelImage.anchor_x = 0#int(self.scaleUnit*9)
        self.laserBarrelImage.anchor_y = int(self.laserBarrelImage.height/2)
        self.laserWidth = self.laserBarrelImage.width
        self.laserBaseImage = pyglet.image.load("./assets/PixelBase.png")
        self.laserBaseImage.anchor_x = int(self.scaleUnit*8)
        self.laserBaseImage.anchor_y = int(self.laserBaseImage.height/2)
        
        self.laserPlatformImage = pyglet.image.load("./assets/PixelPlatform.png")
        self.laserPlatformImage.anchor_x = int(self.scaleUnit*16)
        self.laserPlatformImage.anchor_y = int(self.laserPlatformImage.height/2)


        self.mediaPlayer = pyglet.media.Player()
        self.laserFireAudio = pyglet.media.load('./Assets/LaserShoot.mp3')
        self.laserChargeAudio = pyglet.media.load('./Assets/LaserCharge.mp3')

    def init_sprites(self):
        
        self.laserBarrelSprite = pyglet.sprite.Sprite(img=self.laserBarrelImage, x=self.anchorX, y=self.anchorY)
        #self.laserBarrelSprite.scale = self.laserWidth / self.laserBarrelSprite.width
        self.OGBX = self.laserBarrelSprite.x
        self.OGBY = self.laserBarrelSprite.y

        
        self.laserBaseSprite = pyglet.sprite.Sprite(img=self.laserBaseImage, x=self.anchorX, y=self.anchorY)
        #self.laserBaseSprite.scale = self.laserBaseWidth / self.laserBaseSprite.width

        self.laserPlatformSprite = pyglet.sprite.Sprite(img=self.laserPlatformImage, x=self.anchorX, y=self.anchorY)
        #self.laserPlatformSprite.scale = self.laserBaseWidth / self.laserPlatformSprite.width

        self.laserCharge = pyglet.shapes.Rectangle(x=self.anchorX, y=self.anchorY, width=self.laserWidth, height=self.laserWidth/8, color=(255,0,0))
        self.laserCharge.anchor_x = -self.scaleUnit*2
        self.laserCharge.anchor_y = self.laserCharge.height/2


    def start_laser(self):
        self.charging = True
        
        self.play_sound(self.laserChargeAudio)
    
    def play_sound(self, sound):
        self.mediaPlayer.queue(sound)
        if self.mediaPlayer.playing:
            self.mediaPlayer.next_source()
        self.mediaPlayer.play()
    
    def trim_sound(self):
        if self.mediaPlayer.time >= 2:
            if self.mediaPlayer.volume > 0:
                self.mediaPlayer.volume -= 0.05*(self.mediaPlayer.time - 2)
            elif self.mediaPlayer.volume < 0:
                self.mediaPlayer.volume = 0
        else:
            self.mediaPlayer.volume = 1

    
    def fire_laser(self):
        laser = LaserProjectile(self.laserBarrelSprite.x, self.laserBarrelSprite.y, self.laserWidth*10, self.laserWidth/8, self.getAngleToPlayer())
        self.particleSystemManager.fire_laser(laser)
        self.fired = True
        self.play_sound(self.laserFireAudio)
        

    def reset(self):
        self.fired = False
