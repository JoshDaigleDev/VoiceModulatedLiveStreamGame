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
        self.landscapeManager.update()
        self.particleSystemManager.update(dt)
        self.laserCannonManager.update()
        self.textManager.updateScore(self.gameScore)
        if not self.gameOver:
            self.obstacleManager.update(dt)
            self.textManager.updateLikeTimer(round(10-self.liveManager.likeTimer/60, 1))
        if self.laserCannonManager.fired:
            self.endGame()
            self.textManager.updateLaserCharge(self.laserCannonManager.laserFuel)

        if True:#self.liveManager.connected:
            self.liveManager.update()
            nextEvent = self.liveManager.getNextEvent()
            if nextEvent:
                self.handleNextEvent(nextEvent)
         

    def handleNextEvent(self, event):
        if isinstance(event, FollowEvent):
            print("Follow Event")
            text = f"{event.user} followed!"
            self.textManager.addTempLabel(text)
        if isinstance(event, GiftEvent):
            print("Gift Event")
            text = f"{event.user} donated {event.diamonds} diamonds!"
            self.textManager.addTempLabel(text)
            self.laserCannonManager.fuelLaser(event.diamonds)
            self.textManager.updateLaserCharge(self.laserCannonManager.laserFuel)
        if isinstance(event, LikeEvent):
            print("Like Event")
            goalPercentage = event.amount/event.goal
            difficultyLevel = 4
            if goalPercentage >= 1:
                difficultyLevel = 1
            elif goalPercentage >= 0.5:
                difficultyLevel = 4 - int((goalPercentage - 0.5) * 6)
            text = f"Like Event: Difficulty: {difficultyLevel}"
            self.textManager.addTempLabel(text)
            self.obstacleManager.setDifficulty(difficultyLevel)

    def endGame(self):
        if not self.gameOver:
            self.particleSystemManager.initPlayerExplosion(self.playerManager.playerImage)
        self.gameOver = True
        self.laserCannonManager.reset()

    def startLaser(self):
        if self.laserCannonManager.canFire():
            self.laserCannonManager.start_laser()

    def reset(self):
        self.gameOver = False
        self.gameScore = 0
        self.playerManager.reset()
        self.obstacleManager.reset()
        self.particleSystemManager.reset()
        self.liveManager.reset()

        
    def increaseScore(self):
        self.gameScore += 0.5
