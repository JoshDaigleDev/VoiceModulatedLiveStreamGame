class AudioManager:

    def __init__(self):
        self.highestPitch = 550
        self.normalPitch = 290
        self.lowestPitch = 200
        self.buffer = 25
        self.speed = 75
        
    def pitchToMovement(self, pitch, decibles):
        if decibles < -35:
            return 0
        
        value = min(pitch, self.highestPitch)
        value = max(value, self.lowestPitch)
        value = round(value)

        print(pitch)

        movement = 0

        if value > self.normalPitch - self.buffer and value < self.normalPitch + self.buffer:
            movement = 0
        elif value < self.normalPitch - self.buffer: #low pitch
            if self.normalPitch - value < value - self.lowestPitch:
                movement = -self.speed
            else:
                movement = -2 * self.speed
        elif value > self.normalPitch + self.buffer:
            if self.highestPitch - value < value - self.normalPitch:
                movement = self.speed
            else:
                movement = 2 * self.speed

        return movement
