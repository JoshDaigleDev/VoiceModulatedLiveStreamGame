import pyglet
from pyglet import font
class TextManager():
    
    def __init__(self, dim):
        self.dim = dim
        self.tempLabels = []
        font.add_file('./assets/Perfect DOS VGA 437 Win.ttf')
        self.eightBitFont = font.load('Perfect DOS VGA 437 Win', 64)
        self.initCoordinates()
        self.initLabels()

    def draw(self):
        self.scoreLabel.draw()
        self.laserChargeLabel.draw()
        self.likeTimerLabel.draw()
        for label, _ in self.tempLabels:
            label.draw()

    def updateScore(self, score):
        self.scoreLabel.text = f"{round(score)}"
    
    def updateLaserCharge(self, charge):
        self.laserChargeLabel.text = f"Diamonds: {charge}/10000"
    
    def updateLikeTimer(self, time):
        self.likeTimerLabel.text = f"{time}"
    
    def initCoordinates(self):
        unit, w, h = self.dim.getDimensions()

        self.tempLabelX = 0
        self.tempLabelY = 9*unit

        self.scoreLabelX = 1/2*w
        self.scoreLabelY = 0

        self.laserChargeX = -w
        self.laserChargeY = 3*unit

        self.likeTimerX = -4*unit
        self.likeTimerY = -9*unit
    
    def addTempLabel(self, text):
        label = pyglet.text.Label(
            text,
            font_name=self.eightBitFont.name,
            font_size=self.eightBitFont.size,
            x=self.tempLabelX,
            y=self.tempLabelY,
            anchor_x='center'
            )
        duration = 2
        self.tempLabels.append((label, duration))
        pyglet.clock.schedule_once(lambda dt: self.remove_label(label), duration)
    
    def remove_label(self, label):
        self.tempLabels = [l for l in self.tempLabels if l[0] != label]

    def initLabels(self):
        self.scoreLabel = pyglet.text.Label(
            '0',
            font_name=self.eightBitFont.name,
            font_size=172,
            x=self.scoreLabelX, 
            y=self.scoreLabelY,
            color=(237, 10, 187, 255)
            )
        
        self.laserChargeLabel = pyglet.text.Label(
            "Diamonds: 0/10000", 
            font_name=self.eightBitFont.name,
            font_size=self.eightBitFont.size,
            x=self.laserChargeX,
            y=self.laserChargeY,
            color=(0, 0, 0, 255)
        )

        self.likeTimerLabel = pyglet.text.Label(
            "10",
            font_name=self.eightBitFont.name,
            font_size=self.eightBitFont.size,
            x=self.likeTimerX,
            y=self.likeTimerY,
        )