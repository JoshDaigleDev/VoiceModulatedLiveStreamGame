class LiveManager:
    def __init__(self):
        self.totalLikes = 0
        self.currentLikes = 0
        self.gifts = []
        self.follows = []
    
    def handleGift(self, data):
        print(f"Live Manager: {data.user} GIFTED {data.gift}(${int(data.diamonds)*0.05})")
        pass

    def handleLike(self, data):
        print(f"{data.user} LIKED")
        self.currentLikes += 1
        self.totalLikes += 1
        pass

    def handleFollow(self, data):
        print(f"{data.user} FOLLOWED")
        pass