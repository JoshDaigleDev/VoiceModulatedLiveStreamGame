import pyglet
import math
from LaserProjectile import LaserProjectile
class LaserCannonManager:

    def __init__(self, dim, rendering, playerManager, particleSystemManager, laserHitbox):
        self.dim = dim
        self.batch = rendering[0]
        self.ordering = rendering[1]
        self.playerManager = playerManager
        self.particleSystemManager = particleSystemManager
        self.laserHitbox = laserHitbox
        self.anchorX = int(-17*dim.unit)
        self.anchorY = int(-2*dim.unit)
        self.charging = False
        self.chargeTime = 0
        self.postChargeTime = 0
        self.postChargeMax = 8
        self.maxCharge = 64
        self.postChargeTimeIncrement = 1
        self.reverseCharge = False
        self.postCharging = False
        self.load_assets()
        self.init_sprites()

    def update(self, gameOver):
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
        if not gameOver:
            angle = self.getAngleToTarget(self.laserHitbox.targetX, self.laserHitbox.targetY)
            self.rotateCannon(angle)


    def rotateCannon(self, angle):
        self.laserBarrelSprite.rotation = angle
        self.laserBaseSprite.rotation = angle
        self.laserCharge.rotation = angle

    
    def getAngleToPlayer(self):
        diffX = self.playerManager.player.x - self.laserBarrelSprite.x
        diffY = self.playerManager.player.y - self.laserBarrelSprite.y
        return -math.degrees(math.atan2(diffY, diffX))

    def getAngleToTarget(self, targetX, targetY):
        diffX = targetX - self.laserBarrelSprite.x
        diffY = targetY - self.laserBarrelSprite.y
        return -math.degrees(math.atan2(diffY, diffX))

    def load_assets(self):
        unit, w, h = self.dim.getDimensions()

        # BARREL
        self.laserBarrelImage = pyglet.image.load("./assets/PixelBarrel64.png")
        self.laserBarrelImage.anchor_x = int(-1.8*unit)
        self.laserBarrelImage.anchor_y = int(self.laserBarrelImage.height/2)

        # BASE   
        self.laserBaseImage = pyglet.image.load("./assets/PixelBase64.png")
        self.laserBaseImage.anchor_x = int(1.8*unit)
        self.laserBaseImage.anchor_y = int(self.laserBaseImage.height/2)
        
        # PLATFORM
        self.laserPlatformImage = pyglet.image.load("./assets/PixelPlatform64.png")

        self.laserWidth = self.laserBarrelImage.width*0.75
        self.mediaPlayer = pyglet.media.Player()
        self.laserFireAudio = pyglet.media.load('./Assets/LaserShoot.mp3')
        self.laserChargeAudio = pyglet.media.load('./Assets/LaserCharge.mp3')

    def init_sprites(self):
        unit, w, h = self.dim.getDimensions()

        self.laserBarrelSprite = pyglet.sprite.Sprite(img=self.laserBarrelImage, x=self.anchorX, y=self.anchorY, batch=self.batch, group=self.ordering[6])
        self.laserBaseSprite = pyglet.sprite.Sprite(img=self.laserBaseImage, x=self.anchorX, y=self.anchorY, batch=self.batch, group=self.ordering[7])
        self.laserPlatformSprite = pyglet.sprite.Sprite(img=self.laserPlatformImage, x=-self.dim.w - 0.02*self.dim.unit, y=-5.7*self.dim.unit, batch=self.batch, group=self.ordering[6])
        self.laserCharge = pyglet.shapes.Rectangle(x=self.anchorX, y=self.anchorY, width=self.laserWidth, height=self.laserWidth/8, color=(255,0,0), batch=self.batch, group=self.ordering[5])
        
        self.laserCharge.anchor_x = int(-2.1*unit)
        self.laserCharge.anchor_y = int(self.laserCharge.height/2)


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
        laser = LaserProjectile(self.batch, self.ordering[5], self.laserBarrelSprite.x, self.laserBarrelSprite.y, self.laserWidth*10, self.laserWidth/8, self.getAngleToTarget(self.laserHitbox.targetX, self.laserHitbox.targetY))
        self.particleSystemManager.fire_laser(laser)
        self.play_sound(self.laserFireAudio)

    
    def reset(self):
        self.mediaPlayer.next_source()
