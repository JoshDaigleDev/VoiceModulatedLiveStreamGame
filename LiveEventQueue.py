class LiveEventQueue:
    def __init__(self):
        self.events = []

    def push(self, event):
        self.events.append(event)

    def pop(self):
        return self.events.pop(0)

    def is_empty(self):
        return len(self.events) == 0
