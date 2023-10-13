from EventHelpers import *
from ProgressBar import ProgressBar

class LiveManager:

    def __init__(self, dim, likeCycleDuration, eventDuration):
        self.dim = dim
        self.duration = eventDuration
        self.connected = False
        self.totalLikes = 0 #Total Likes for duration of stream
        self.currentLikes = 0 #Likes for current cycle
        self.likeAmount = 0 #Final like amount for prevous cycle 
        self.likeGoal = 50
        self.liveEventQueue = LiveEventQueue(self.duration)
        self.diamondThreshhold = 199
        self.likeDuration = likeCycleDuration
        self.likeTimer = self.likeDuration
        self.cycleFinished = False


    def getNextEvent(self):
        nextEvent = None
        if self.cycleFinished:
            nextEvent = LikeEvent(self.likeAmount, self.likeGoal)
            self.likeAmount = 0
            self.cycleFinished = False
        elif self.liveEventQueue.isReady:
            nextEvent = self.liveEventQueue.dequeue()
        return nextEvent
    

    def update(self):
        self.liveEventQueue.update()
    

    def finishCycle(self):
        self.likeAmount = self.currentLikes
        self.currentLikes = 0
        self.cycleFinished = True


    def handleGift(self, data):
        user = data['user']
        gift = data['gift']
        diamonds = int(data['diamonds'])
        #print(f"Live Manager: {user} GIFTED {gift}({diamonds} Diamonds = ${diamonds*0.005})")

        if diamonds >= self.diamondThreshhold:
            event = GiftEvent(user, gift, diamonds)
            self.liveEventQueue.enqueue(event)


    def handleLike(self, data):
        #print(f"Live Manager: {data['user']}: LIKED")
        totalLikes = self.format_integer(data['totalLikes'])
        print(f"LIKES: {totalLikes}")
        self.currentLikes += 1
        self.totalLikes += 1


    def handleFollow(self, data):
        user = data['user']       
        event = FollowEvent(user)
        self.liveEventQueue.enqueue(event)


    def handleConnected(self):
        self.connected = True

    
    def reset(self):
        self.likeTimer = 0
        self.currentLikes = 0
        self.likeAmount = 0


    def format_integer(self, n):
        if n < 1000:
            return str(n)
        elif n < 1000000:
            decimal_part = (n % 1000) // 100
            if decimal_part > 0:
                return f"{n // 1000}.{decimal_part}k"
            else:
                return f"{n // 1000}k"
        else:
            decimal_part = (n % 1000000) // 100000
            if decimal_part > 0:
                return f"{n // 1000000}.{decimal_part}M"
            else:
                return f"{n // 1000000}M"

