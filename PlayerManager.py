import pyglet
from Player import Player

class PlayerManager:
    
    def __init__(self, dim, rendering):
        self.dim = dim
        self.batch = rendering[0]
        self.ordering = rendering[1]
        self.ORIGIN_X = 0
        self.ORIGIN_Y = 0
        self.playerImage = pyglet.image.load('./assets/PlayerIconVibe.png')
        self.playerImage.anchor_x = self.playerImage.width // 2 
        self.playerImage.anchor_y = self.playerImage.height // 2 
        self.playerSprite = pyglet.sprite.Sprite(img=self.playerImage, x=self.ORIGIN_X, y=self.ORIGIN_Y, batch=self.batch, group=self.ordering[9])
        self.player = Player(self.ORIGIN_X, self.ORIGIN_Y, self.playerSprite)


    def movePlayer(self, movement, direction):
        if not self.player.dead:
            if movement > 0 and self.player.y + self.player.radius < self.dim.h:
                self.player.move(0, movement, direction)
            elif movement < 0 and self.player.y - self.player.radius > -self.dim.h:
                self.player.move(0, movement, direction)
            self.player.update()


    def reset(self):
        playerSprite = pyglet.sprite.Sprite(img=self.playerImage, x=self.ORIGIN_X, y=self.ORIGIN_Y, batch=self.batch, group=self.ordering[9])
        self.player.reset(self.ORIGIN_X, self.ORIGIN_Y)
        self.player.sprite = playerSprite
    

    def destruct(self):
        self.player.dead = True
        self.player.sprite.delete()


