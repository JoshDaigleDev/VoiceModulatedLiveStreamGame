from EventHelpers import *
from ProgressBar import ProgressBar

class LiveManager:
    def __init__(self, dim, duration):
        self.dim = dim
        self.duration = duration
        self.connected = False
        self.totalLikes = 0 #Total Likes for duration of stream
        self.currentLikes = 0 #Likes for current cycle
        self.likeAmount = 0 #Final like amount for prevous cycle 
        self.likeGoal = 50
        self.liveEventQueue = LiveEventQueue(self.duration)
        self.diamondThreshhold = 299
        self.likeDuration = 10 * 60
        self.likeTimer = 0
        self.cycleFinished = False
        self.initProgressBar(dim, self.likeGoal)
        self.showProgressBar = True
        self.progressBarHideTimer = 0

    def initProgressBar(self, dim, likeGoal):
        likeProgressMaxUnits = 28
        likeProgressX = -12*dim.unit
        likeProgressY = -9*dim.unit
        self.likeProgress = ProgressBar(dim=dim, x=likeProgressX, y=likeProgressY, unitLen=likeProgressMaxUnits, maxProgress=likeGoal) 


    def draw(self):
        if self.showProgressBar:
            self.likeProgress.draw()
    
    def updateHideProgressBarTimer(self):
        if self.progressBarHideTimer > 0:
            self.showProgressBar = False
            self.progressBarHideTimer -= 1
        else:
            self.showProgressBar = True
    
    def getNextEvent(self):
        nextEvent = None
        if self.cycleFinished:
            nextEvent = LikeEvent(self.likeAmount, self.likeGoal)
            self.likeAmount = 0
            self.cycleFinished = False
        elif self.liveEventQueue.isReady:
            nextEvent = self.liveEventQueue.dequeue()
        return nextEvent
    
    def setHideProgressBarTimer(self, duration):
        self.progressBarHideTimer = duration
    
    def update(self):
        self.liveEventQueue.update()
        self.updateLikeCycles()
        self.updateHideProgressBarTimer()
    
    def updateLikeCycles(self):
        self.likeTimer += 1
        if self.likeTimer >= self.likeDuration:
            self.likeProgress.reset()
            self.likeTimer = 0
            self.likeAmount = self.currentLikes
            self.currentLikes = 0
            self.cycleFinished = True

    def handleGift(self, data):
        user = data['user']
        gift = data['gift']
        diamonds = int(data['diamonds'])
        print(f"Live Manager: {user} GIFTED {gift}({diamonds} Diamonds = ${diamonds*0.005})")

        if diamonds >= self.diamondThreshhold:
            event = GiftEvent(user, gift, diamonds)
            self.liveEventQueue.enqueue(event)


    def handleLike(self, data):
        print(f"Live Manager: {data['user']}: LIKED")
        self.currentLikes += 1
        self.totalLikes += 1
        self.likeProgress.increment(1)


    def handleFollow(self, data):
        user = data['user']
        print(f"Live Manager: {user}: FOLLOWED")
        event = FollowEvent(user)
        self.liveEventQueue.enqueue(event)

    def handleConnected(self):
        self.connected = True
    
    def reset(self):
        self.likeTimer = 0
        self.currentLikes = 0
        self.likeAmount = 0
        self.likeProgress.reset()