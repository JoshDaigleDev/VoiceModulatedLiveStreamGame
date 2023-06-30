from ObstacleManager import ObstacleManager
from PlayerManager import PlayerManager
from ParticleSystemManager import ParticleSystemManager
from TextManager import TextManager
from LaserCannonManager import LaserCannonManager
from LandscapeManager import LandscapeManager
from LiveManager import LiveManager

from EventHelpers import FollowEvent, GiftEvent, LikeEvent
class Game:

    def __init__(self, dim):
        self.eventDuration = 3
        self.dim = dim
        self.playerManager = PlayerManager(self.dim)
        self.obstacleManager = ObstacleManager(self.dim)
        self.particleSystemManager = ParticleSystemManager(self.dim, self.playerManager.player, self.obstacleManager)
        self.textManager = TextManager(self.dim)
        self.laserCannonManager = LaserCannonManager(self.dim, self.playerManager, self.particleSystemManager)
        self.landscapeManager = LandscapeManager(self.dim)
        self.liveManager = LiveManager(self.dim, self.eventDuration)
        self.gameOver = False
        self.gameScore = 0
        self.CANNON_DIAMOND_AMOUNT = 500
        self.HARDMODE_DIAMOND_AMOUNT = 1000
        self.HARDMODE_DURATION = 30 * 60


    def draw(self):
        self.landscapeManager.draw()
        self.particleSystemManager.draw()
        self.obstacleManager.draw()
        self.laserCannonManager.draw()
        self.textManager.draw()
        self.liveManager.draw()
        if not self.gameOver:
            self.playerManager.draw()


    def update(self, dt):
        self.particleSystemManager.update(dt)
        self.textManager.updateScore(self.gameScore)
        self.laserCannonManager.update()
        if not self.gameOver:
            self.landscapeManager.update()
            self.obstacleManager.update(dt)
            if not self.obstacleManager.hardmode:
                self.textManager.updateTimer(round(self.liveManager.likeTimer/60, 1))
            else:
                self.textManager.updateTimer(round(self.obstacleManager.hardmodeTimer/60, 1))
        if self.laserCannonManager.fired:
            self.endGame()
            self.textManager.updateTimer(10)
        if True:#self.liveManager.connected:
            self.liveManager.update()
            nextEvent = self.liveManager.getNextEvent()
            if nextEvent:
                self.handleNextEvent(nextEvent)
        

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
        self.gameOver = True
        self.laserCannonManager.reset()

    def startLaser(self):
        self.laserCannonManager.start_laser()

    def reset(self):
        self.gameOver = False
        self.gameScore = 0
        self.playerManager.reset()
        self.obstacleManager.reset()
        self.particleSystemManager.reset()
        if not self.obstacleManager.hardmode:
            self.liveManager.reset()

        
    def increaseScore(self):
        self.gameScore += 0.5


    def handleGiftEvent(self, event):
        print("Gift Event")
        text = f"{event.user} donated {event.diamonds} diamonds!"
        self.textManager.addTempLabel(text, 8)
        if event.diamonds == self.CANNON_DIAMOND_AMOUNT:
            self.laserCannonManager.start_laser()
            text = f"{event.user} Fired The Laser Cannon!"
            self.textManager.addTempLabel(text, 4)
        elif event.diamonds == self.HARDMODE_DIAMOND_AMOUNT:
            self.liveManager.setHideProgressBarTimer(self.HARDMODE_DURATION)
            text = f"{event.user} Has Activated Hardmode!"
            self.textManager.addTempLabel(text, -9, 5, (255, 0, 0, 255))
            self.obstacleManager.activateHardmode(self.HARDMODE_DURATION)


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
            if self.liveManager.showProgressBar:
                self.liveManager.setHideProgressBarTimer(120)
                self.textManager.addTempLabel(text, -9, color=textColor)
            self.obstacleManager.setDifficulty(difficultyLevel)