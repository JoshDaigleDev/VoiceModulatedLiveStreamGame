class LiveEvent:
    def __init__(self):
        self.done = False
        self.duration = 1

class DonationEvent(LiveEvent):
    def __init__(self, diamonds):
        super().__init__()
        self.diamonds = diamonds 