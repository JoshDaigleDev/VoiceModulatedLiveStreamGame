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
        self.likeGoal = 10
        self.liveEventQueue = LiveEventQueue(self.duration)
        self.diamondThreshhold = 500
        self.likeDuration = 10 * 60
        self.likeTimer = 0
        self.initProgressBar(dim, self.likeGoal)

    def initProgressBar(self, dim, likeGoal):
        likeProgressMaxUnits = 20
        likeProgressX = -13*dim.unit
        likeProgressY = -9*dim.unit
        green = (0, 255, 0)
        self.likeProgress = ProgressBar(dim=dim, x=likeProgressX, y=likeProgressY, colour=green, unitLen=likeProgressMaxUnits, maxProgress=likeGoal)


    def draw(self):
        self.likeProgress.draw()
    
    def getNextEvent(self):
        nextEvent = None
        if self.likeAmount > 0:
            nextEvent = LikeEvent(self.likeAmount)
            self.likeAmount = 0
        elif self.liveEventQueue.isReady:
            nextEvent = self.liveEventQueue.dequeue()
        return nextEvent
    
    def update(self):
        self.liveEventQueue.update()
        self.likeTimer += 1
        if self.likeTimer >= self.likeDuration:
            self.likeProgress.reset()
            self.likeTimer = 0
            self.likeAmount = self.currentLikes
            self.currentLikes = 0
            

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