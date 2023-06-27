import time
class LiveEventQueue:
    def __init__(self, duration):
        self.duration = duration
        self.queue = []
        self.lastPop = time.time()
        self.eventDuration = 3
        self.isReady = False

    def enqueue(self, event):
        self.queue.append(event)

    def update(self):
        if not self.isEmpty():
            currTime = time.time()
            if currTime - self.lastPop >= self.eventDuration:
                self.isReady = True


    def dequeue(self):
        if self.isReady:
            self.lastPop = time.time()
            self.isReady = False
            return self.queue.pop(0)


    def isEmpty(self):
        return len(self.queue) == 0
    

class LiveEvent:
    def __init__(self):
        pass
        

class GiftEvent(LiveEvent):
    def __init__(self, user, gift, diamonds):
        super().__init__()
        self.user = user
        self.giftType = gift
        self.diamonds = diamonds

class FollowEvent(LiveEvent):
    def __init__(self, user):
        super().__init__()
        self.user = user

class LikeEvent(LiveEvent):
    def __init__(self, amount, goal):
        super().__init__()
        self.amount = amount
        self.goal = goal
