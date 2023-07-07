from ObstacleManager import ObstacleManager
from PlayerManager import PlayerManager
from ParticleSystemManager import ParticleSystemManager
from TextManager import TextManager
from LaserCannonManager import LaserCannonManager
from LandscapeManager import LandscapeManager
from LiveManager import LiveManager
from ProgressBarManager import ProgressBarManager
from LaserHitBox import LaserHitBox
from GameScoreManager import GameScoreManager

from EventHelpers import FollowEvent, GiftEvent, LikeEvent
class Game:

    def __init__(self, dim, rendering):
        self.dim = dim
        self.rendering = rendering
        self.playerManager = PlayerManager(self.dim, self.rendering) #
        self.obstacleManager = ObstacleManager(self.dim, self.rendering) #
        self.laserAnchorX = -17*dim.unit
        self.laserAnchorY = -2*dim.unit
        self.laserHitbox = LaserHitBox(self.dim, self.laserAnchorX, self.laserAnchorY) # 
        self.particleSystemManager = ParticleSystemManager(self.dim, self.rendering, self.playerManager.player, self.obstacleManager)
        self.textManager = TextManager(self.dim, self.rendering) #?
        self.laserCannonManager = LaserCannonManager(self.dim, self.rendering, self.playerManager, self.particleSystemManager, self.laserHitbox) #
        self.landscapeManager = LandscapeManager(self.dim, self.rendering)
        self.progressBarManager = ProgressBarManager(self.dim) #?
        self.gameScoreManager = GameScoreManager()
        self.textManager.updateHighScore(self.gameScoreManager.highScore)
        self.gameOver = False
        self.CANNON_DIAMOND_AMOUNT = 199
        self.HARDMODE_DIAMOND_AMOUNT = 1000
        self.HARDMODE_DURATION = 30 * 60
        self.LIKE_GOAL = 50
        self.LIKE_DURATION = 10 * 60
        self.EVENT_DURATION = 3
        self.likeTimer = self.LIKE_DURATION
        self.hardTimer =  self.HARDMODE_DURATION
        self.liveManager = LiveManager(self.dim, self.LIKE_DURATION, self.EVENT_DURATION)
        self.progressBarManager.initLikeBar(self.LIKE_GOAL)
        self.progressBarManager.initHardBar(self.HARDMODE_DURATION / 60)
        self.hardMode = False
        self.obstacleManager.setDifficulty(2)


    def draw(self):
        self.rendering[0].draw()
        self.textManager.draw()
        self.progressBarManager.draw()
        if self.gameOver:
            self.textManager.drawPlayAgain()
        else:
            self.textManager.drawScoreLabel()

    def update(self, dt):
        self.particleSystemManager.update(dt)
        self.laserCannonManager.update(self.gameOver)
        self.liveManager.update()
        self.laserHitbox.update(self.particleSystemManager.activeLaser(), self.gameOver)

        nextEvent = self.liveManager.getNextEvent()
        if nextEvent:
            self.handleNextEvent(nextEvent)
        
        if not self.gameOver:
            self.landscapeManager.update()
            self.obstacleManager.update(self.hardMode)
            self.updateHardCycle()
            self.updateLikeCycle()
            self.progressBarManager.update()
            if not self.hardMode:
                self.textManager.updateTimer(round(self.likeTimer/60, 1))
            else:
                self.textManager.updateTimer(round(self.hardTimer/60, 1))
        else:
            self.landscapeManager.updateClouds(0.2)
            
        if self.laserHitbox.hit(self.playerManager.player):
            print("INTERCEPTION!!!!")


    def handleNextEvent(self, event):
        if isinstance(event, FollowEvent):
            self.handleFollowEvent(event)
        if isinstance(event, GiftEvent):
            self.handleGiftEvent(event)
        if isinstance(event, LikeEvent):
            self.handleLikeEvent(event)

    def endGame(self):
        if not self.gameOver:
            self.particleSystemManager.initPlayerExplosion(self.playerManager.playerImage)
            if not self.playerManager.player.dead:
                self.playerManager.destruct()
        self.gameOver = True

    def startLaser(self):
        self.laserCannonManager.start_laser()

    def reset(self):
        self.gameOver = False
        self.gameScoreManager.reset()
        self.playerManager.reset()
        self.obstacleManager.reset()
        self.particleSystemManager.reset()
        self.liveManager.reset()
        self.progressBarManager.resetLikes()
        self.laserCannonManager.reset()
        self.likeTimer = self.LIKE_DURATION
        if self.hardMode:
            self.obstacleManager.run = True
        else:
            self.obstacleManager.setDifficulty(2)

        
    def increaseScore(self):
        self.gameScoreManager.incrementScore(0.5)
        self.textManager.updateScore(self.gameScoreManager.score)
        self.textManager.updateHighScore(self.gameScoreManager.highScore)
 

    def handleGiftEvent(self, event):
        print("Gift Event")

        if event.diamonds == self.CANNON_DIAMOND_AMOUNT:
            self.laserCannonManager.start_laser()
            text = f"{event.user} Fired The Laser Cannon!"
            self.textManager.addTempLabel(text, 8, color=(255, 0, 0, 255))
        elif event.diamonds == self.HARDMODE_DIAMOND_AMOUNT:
            self.hardMode = True
            self.progressBarManager.showHardBar = True
            self.progressBarManager.showLikeBar = False
            self.obstacleManager.setDifficulty(4)
            self.hardTimer = self.HARDMODE_DURATION
            text = f"{event.user} Has Activated Hardmode!"
            self.textManager.addTempLabel(text, 8, color=(255, 0, 0, 255))
        else:
            text = f"{event.user} donated {event.diamonds} diamonds!"
            self.textManager.addTempLabel(text, 8)



    def handleFollowEvent(self, event):
        print("Follow Event")
        text = f"{event.user} followed!"
        self.textManager.addTempLabel(text, 8)


    def handleLikeEvent(self, event):
        print("Like Event")
        goalPercentage = event.amount/event.goal
        difficulty = "Hard"
        textColor = (255, 255, 255, 255)
        if goalPercentage >= 1:
            difficultyLevel = 1
            difficulty = "Easy"
            textColor = (0, 255, 255, 255)
        elif goalPercentage >= 0.7:
            difficultyLevel = 2
            difficulty = "Normal"
            textColor = (0, 255, 0, 255)
        elif goalPercentage >= 0.4:
            difficultyLevel = 3
            difficulty = "Tough"
            textColor = (255, 255, 0, 255)
        else:
            difficultyLevel = 4
            difficulty = "Hard"
            textColor = (255, 0, 0, 255)

        text = f"Difficulty: {difficulty}"
        if not self.gameOver:
            self.progressBarManager.hideLikeBar(120)
            self.textManager.addTempLabel(text, -9, color=textColor)
            self.obstacleManager.setDifficulty(difficultyLevel)
    

    def individualLike(self):
        self.progressBarManager.likeBar.increment(1)
        print("LIke")
    
    def updateLikeCycle(self):
        if not self.hardMode:
            self.likeTimer -= 1
            if self.likeTimer <= 0:
                self.likeTimer = self.LIKE_DURATION
                self.liveManager.finishCycle()
                self.progressBarManager.resetLikes()

    def updateHardCycle(self):
        if self.hardMode:
            self.hardTimer -= 1
            self.progressBarManager.hardBar.setAmount(self.hardTimer / 60)
            if self.hardTimer <= 0:
                self.hardTimer = self.HARDMODE_DURATION
                self.hardMode = False
                self.progressBarManager.showHardBar = False
                self.progressBarManager.showLikeBar = True