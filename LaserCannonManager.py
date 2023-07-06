import pyglet
import math
from LaserProjectile import LaserProjectile
class LaserCannonManager:

    def __init__(self, dim, playerManager, particleSystemManager, laserHitbox):
        self.dim = dim
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
        self.fired = False
        self.reverseCharge = False
        self.postCharging = False
        self.load_assets()
        self.init_sprites()
        self.laserFuel = 0
        self.maxFuel = 1000


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
        unit, w, h = self.dim.getDimensions()

        # BARREL
        self.laserBarrelImage = pyglet.image.load("./assets/PixelBarrel64.png")
        self.laserBarrelImage.anchor_x = -4*unit
        self.laserBarrelImage.anchor_y = int(self.laserBarrelImage.height/2)

        # BASE   
        self.laserBaseImage = pyglet.image.load("./assets/PixelBase64.png")
        self.laserBaseImage.anchor_x = unit
        self.laserBaseImage.anchor_y = int(self.laserBaseImage.height/2)
        
        # PLATFORM
        self.laserPlatformImage = pyglet.image.load("./assets/PixelPlatform64.png")

        self.laserWidth = self.laserBarrelImage.width*0.75
        self.mediaPlayer = pyglet.media.Player()
        self.laserFireAudio = pyglet.media.load('./Assets/LaserShoot.mp3')
        self.laserChargeAudio = pyglet.media.load('./Assets/LaserCharge.mp3')

    def init_sprites(self):
        unit, w, h = self.dim.getDimensions()

        self.laserBarrelSprite = pyglet.sprite.Sprite(img=self.laserBarrelImage, x=self.anchorX, y=self.anchorY)
        self.laserBaseSprite = pyglet.sprite.Sprite(img=self.laserBaseImage, x=self.anchorX, y=self.anchorY)
        self.laserPlatformSprite = pyglet.sprite.Sprite(img=self.laserPlatformImage, x=-self.dim.w - 1/4*self.dim.unit, y=-7*self.dim.unit)
        self.laserCharge = pyglet.shapes.Rectangle(x=self.anchorX, y=self.anchorY, width=self.laserWidth, height=self.laserWidth/8, color=(255,0,0))
        
        self.laserCharge.anchor_x = -4*unit
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
        laser = LaserProjectile(self.laserBarrelSprite.x, self.laserBarrelSprite.y, self.laserWidth*10, self.laserWidth/8, self.getAngleToTarget(self.laserHitbox.targetX, self.laserHitbox.targetY))
        self.particleSystemManager.fire_laser(laser)
        self.fired = True
        self.play_sound(self.laserFireAudio)
        self.laserFuel = 0

    
    def fuelLaser(self, diamonds):
        self.laserFuel = min(self.maxFuel, self.laserFuel + diamonds)
    

    def canFire(self):
        return self.laserFuel >= self.maxFuel


    def reset(self):
        self.fired = False
        self.laserFuel = 0
