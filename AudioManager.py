class AudioManager:

    def __init__(self):
        self.highestPitch = 550
        self.normalPitch = 290
        self.lowestPitch = 200
        self.buffer = 25
        self.speed = 75
        
    def pitchToMovement(self, pitch, decibles):

        movement = -self.speed/2
        direction = 1
        sound = False

        if decibles < -35:
            return movement, direction, sound
        
        value = min(pitch, self.highestPitch)
        value = max(value, self.lowestPitch)
        value = round(value)

        if value > self.normalPitch - self.buffer and value < self.normalPitch + self.buffer:
            movement = 0
            direction = 0
            sound = True
        elif value < self.normalPitch - self.buffer: #low pitch
            if self.normalPitch - value < value - self.lowestPitch:
                movement = -self.speed
            else:
                movement = - self.speed
            direction = 1
            sound = True
        elif value > self.normalPitch + self.buffer:
            if self.highestPitch - value < value - self.normalPitch:
                movement = 3*self.speed
            else:
                movement = 2*self.speed
            direction = -1
            sound = True

        return movement, direction, sound
