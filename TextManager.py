import pyglet
from pyglet import font
class TextManager():
    
    def __init__(self, dim, rendering):
        self.dim = dim
        self.batch = rendering[0]
        self.ordering = rendering[1]
        self.tempLabels = []
        font.add_file('./assets/Perfect DOS VGA 437 Win.ttf')
        self.eightBitFont = font.load('Perfect DOS VGA 437 Win', 64)
        self.initCoordinates()
        self.initLabels()
        self.initShapes()


    def initShapes(self):
        unit = self.dim.unit
        self.cannonBG = pyglet.shapes.Rectangle(self.laserChargeX-0.5*unit, self.laserChargeY-0.5*unit, 9*unit, 1.5*unit, color=(0,0,0,255), batch=self.batch, group=self.ordering[8])
        self.difficultyBG = pyglet.shapes.Rectangle(self.difficultyX-0.5*unit, self.difficultyY-0.5*unit, 10*unit, 1.5*unit, color=(0,0,0,255), batch=self.batch, group=self.ordering[8])


    def drawScoreLabel(self):
        self.scoreLabel.draw()


    def drawPlayAgain(self):
        unit = self.dim.unit
        backDropX = -7*unit
        backDropY = -2*unit

        backDropImage = pyglet.image.load("./Assets/GameOverBG.png")
        backDropImage.anchor_x = 0
        backDropImage.anchor_y = 0
        backDropSprite = pyglet.sprite.Sprite(backDropImage, backDropX, backDropY)

        backDropSprite.draw()
        
        self.tryAgainLabel.draw()
        self.highScoreLabel.draw()


    def updateScore(self, score):
        self.scoreLabel.text = f"{round(score)}"
    

    def updateHighScore(self, score):
        self.highScoreLabel.text = f"High Score: {round(score)}"
    

    def updateTimer(self, time):
        self.timerLabel.text = f"{time}"
    

    def initCoordinates(self):
        unit, w, h = self.dim.getDimensions()

        self.tempLabelX = 0
        self.tempLabelY = 8*unit

        self.scoreLabelX = 10*unit
        self.scoreLabelY = 0

        self.highScoreLabelX = -4.5*unit
        self.highScoreLabelY = -0.7*unit

        self.tryAgainLabelX = -4.6*unit
        self.tryAgainLabelY = 1.3*unit

        self.laserChargeX = -19*unit
        self.laserChargeY = 3*unit

        self.difficultyX = -19*unit
        self.difficultyY = 5*unit

        self.diamondEmojiCanX = -11.8*unit
        self.diamondEmojiDifX = -10.8*unit

        self.likeLabelX = 15*unit
        self.likeLabelY = -8.8*unit

        self.timerX = -17*unit
        self.timerY = -9*unit
    

    def draw(self):
        self.laserChargeLabel.draw()
        self.timerLabel.draw()
        self.difficultyLabel.draw()
        self.diamondEmojiDifficulty.draw()
        self.diamondEmojiCannon.draw()
        self.likeLabel.draw()
        if len(self.tempLabels) > 0:
            for label, _ in self.tempLabels:
                label.draw()
        else: 
            self.streamTitleLabel.draw()
                 

    def addTempLabel(self, text, positionUnits, duration=2, color=(255,255,255,255)):
        positionY = positionUnits*self.dim.unit
        label = pyglet.text.Label(
            text,
            font_name=self.eightBitFont.name,
            font_size=self.eightBitFont.size,
            x=self.tempLabelX,
            y=positionY,
            anchor_x='center',
            color=color
            )
        self.tempLabels.append((label, duration))
        pyglet.clock.schedule_once(lambda dt: self.remove_label(label), duration)
    

    def remove_label(self, label):
        self.tempLabels = [l for l in self.tempLabels if l[0] != label]


    def initLabels(self):
        self.streamTitleLabel = pyglet.text.Label(
            'Voice Controlled Challenge! Like To Help!',
            font_name=self.eightBitFont.name,
            font_size=60,
            x=self.laserChargeX, 
            y=self.tempLabelY,
            color=(255, 255, 255, 255)
        )
        
        self.likeLabel = pyglet.text.Label(
            '← Like!',
            font_name=self.eightBitFont.name,
            font_size=42,
            x=self.likeLabelX, 
            y=self.likeLabelY,
            color=(255, 255, 255, 255)
        )

        self.scoreLabel = pyglet.text.Label(
            '0',
            font_name=self.eightBitFont.name,
            font_size=172,
            x=self.scoreLabelX, 
            y=self.scoreLabelY,
            color=(0, 0, 0, 255)
        )
        
        self.highScoreLabel = pyglet.text.Label(
            'High Score: 0',
            font_name=self.eightBitFont.name,
            font_size=44,
            x=self.highScoreLabelX, 
            y=self.highScoreLabelY,
            color=(0, 0, 0, 255)
        )
        
        self.tryAgainLabel = pyglet.text.Label(
            'Game Over!',
            font_name=self.eightBitFont.name,
            font_size=64,
            x=self.tryAgainLabelX, 
            y=self.tryAgainLabelY,
            color=(0, 0, 0, 255)
        )
        
        self.laserChargeLabel = pyglet.text.Label(
            "Fire Cannon:199", 
            font_name=self.eightBitFont.name,
            font_size=32,
            x=self.laserChargeX,
            y=self.laserChargeY,
            color=(255, 255, 255, 255)
        )

        self.difficultyLabel = pyglet.text.Label(
            "30s Hardmode:1000", 
            font_name=self.eightBitFont.name,
            font_size=32,
            x=self.difficultyX,
            y=self.difficultyY,
            color=(255, 255, 255, 255)
        )

        self.diamondEmojiCannon = pyglet.text.Label(
            "💎",
            font_size=32,
            x=self.diamondEmojiCanX,
            y=self.laserChargeY
        )
        
        self.diamondEmojiDifficulty = pyglet.text.Label(
            "💎",
            font_size=32,
            x=self.diamondEmojiDifX,
            y=self.difficultyY
        )

        self.timerLabel = pyglet.text.Label(
            "10",
            font_name=self.eightBitFont.name,
            font_size=self.eightBitFont.size,
            x=self.timerX,
            y=self.timerY,
        )