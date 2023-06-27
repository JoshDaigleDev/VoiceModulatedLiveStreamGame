import pyglet
from pyglet import font
class TextManager():
    
    def __init__(self, window):
        self.window = window
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
        self.laserChargeLabel.text = f"💎: {charge}/10000"
    
    def updateLikeTimer(self, time):
        self.likeTimerLabel.text = f"{time}"
    
    def initCoordinates(self):
        self.tempLabelX = 0
        self.tempLabelY = self.window.height/2.3

        self.scoreLabelX = self.window.width/4
        self.scoreLabelY = 0

        self.laserChargeX = -self.window.width/2
        self.laserChargeY = self.window.height/12

        self.likeTimerX = -self.window.width/10
        self.likeTimerY = -self.window.height/2 + self.window.height/16
    
    def addTempLabel(self, text):
        label = pyglet.text.Label(
            text,
            font_name=self.eightBitFont.name,
            font_size=self.eightBitFont.size,
            x=self.tempLabelX,
            y=self.tempLabelY,
            anchor_x='center',
            anchor_y='center'
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
            "💎: 0/10000", 
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