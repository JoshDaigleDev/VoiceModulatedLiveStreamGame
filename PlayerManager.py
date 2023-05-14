from Player import Player

class PlayerManager:
    def __init__(self, window):
        self.window = window
        self.ORIGIN_X = window.width/-4
        self.ORIGIN_Y = 0
        self.player = Player(self.ORIGIN_X, self.ORIGIN_Y)

    def movePlayer(self, movement):
        if movement > 0 and self.player.y + self.player.radius < self.window.height/2:
            self.player.move(0, movement)
        elif movement < 0 and self.player.y - self.player.radius > -self.window.height/2:
            self.player.move(0, movement)

            
    def draw(self):
        self.player.draw()
    


