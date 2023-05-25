import pyglet
from Player import Player

class PlayerManager:
    def __init__(self, window):
        self.window = window
        self.ORIGIN_X = window.width/-4
        self.ORIGIN_Y = 0
        self.playerImage = pyglet.image.load('./assets/PlayerSprite.png')
        self.playerImage.anchor_x = self.playerImage.width // 2 ##this line is new
        self.playerImage.anchor_y = self.playerImage.height // 2 ## and this line also
        self.playerSprite = pyglet.sprite.Sprite(img=self.playerImage, x=self.ORIGIN_X, y=self.ORIGIN_Y)
        self.playerSprite.scale = 100 / self.playerSprite.width
        self.player = Player(self.ORIGIN_X, self.ORIGIN_Y, self.playerSprite)

    def movePlayer(self, movement, direction):
        if movement > 0 and self.player.y + self.player.radius < self.window.height/2:
            self.player.move(0, movement, direction)
        elif movement < 0 and self.player.y - self.player.radius > -self.window.height/2:
            self.player.move(0, movement, direction)
        self.player.update()

    def draw(self):
        self.player.draw()
    
    def reset(self):
        self.player.reset(self.ORIGIN_X, self.ORIGIN_Y)
    


