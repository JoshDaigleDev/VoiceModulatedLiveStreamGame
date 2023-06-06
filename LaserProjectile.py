import math 
import pyglet
class LaserProjectile():
    
    def __init__(self, x, y, width, height, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cycle = math.pi/30
        self.cycle2 = 0
        self.scaler = 0
        self.dead = False
        #self.rectangle.anchor_x = self.x
        #self.rectangle.anchor_y = self.y
        self.angle = angle 
        self.laserY = self.y
        self.colorOpacity = 0
        self.color1 = 0
        self.color2 = 255
        self.color3 = 127

    def draw(self):
        #self.rectangle.rotation = self.angle
        rect = pyglet.shapes.Rectangle(self.x, self.laserY, self.width, self.scaler, color=(self.colorOpacity, 0, self.color2, self.colorOpacity))
        rect.rotation = self.angle
        rect.draw()

    def update(self):
        self.cycle += math.pi/20
        self.cycle2 += math.pi/90
        self.scaler = self.height * math.sin(self.cycle)
        self.scaler2 = self.height * math.sin(self.cycle2)
        if math.sin(self.cycle) <= 0: 
            self.dead = True
        

        self.laserY = self.y - self.scaler / 2
        self.laserHeight = self.scaler
        self.colorOpacity = int(255 * math.sin(self.cycle))
        self.color2 = int(255 * math.cos(self.cycle/2))
        self.color3 = int(255 * math.sin(self.cycle*2))


