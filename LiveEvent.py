class LiveEvent:
    def __init__(self, user):
        self.user = user
        self.done = False
        self.duration = 0

class GiftEvent(LiveEvent):
    def __init__(self, user, diamonds):
        super().__init__(user)
        self.giftType = None
        self.diamonds = diamonds
        self.duration = 3

class LikeEvent:
    def __init__(self, user):
        super().__init__(user)

class FollowEvent:
    def __init__(self, user):
        super().__init__(user)