import pyglet
from Player import Player

class PlayerManager:
    def __init__(self, window):
        self.window = window
        self.ORIGIN_X = window.width/-4
        self.ORIGIN_Y = 0
        self.playerAnimation = pyglet.image.load('./assets/TriangleIcon1.png')
        self.playerSprite = pyglet.sprite.Sprite(img=self.playerAnimation, x=self.ORIGIN_X+50, y=self.ORIGIN_Y-50)
        self.playerSprite.scale = 100 / self.playerSprite.width
        self.player = Player(self.ORIGIN_X, self.ORIGIN_Y, self.playerSprite)

    def movePlayer(self, movement):
        if movement > 0 and self.player.y + self.player.radius < self.window.height/2:
            self.player.move(0, movement)
        elif movement < 0 and self.player.y - self.player.radius > -self.window.height/2:
            self.player.move(0, movement)
        self.player.update()

    def draw(self):
        self.player.draw()
    
    def reset(self):
        self.player.reset(self.ORIGIN_X, self.ORIGIN_Y)
    


