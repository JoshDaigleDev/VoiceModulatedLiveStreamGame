class AudioManager:

    def __init__(self):
        self.highestPitch = 600
        self.normalPitch = 350
        self.lowestPitch = 150
        self.buffer = 50
        self.speed = 100


    def pitchToMovement(self, pitch, decibles):
        if decibles < -40:
            return 0
        
        value = min(pitch, self.highestPitch)
        value = max(pitch, self.lowestPitch)
        value = round(pitch)

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
