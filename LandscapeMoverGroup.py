import pyglet 
from Mover import Mover

class LandscapeMoverGroup:

    def __init__(self, dim, batch, group, imgWidth, speed, positionX, positionY):
        self.dim = dim
        self.batch = batch
        self.group = group
        self.movers = []
        self.moverWidth = imgWidth
        self.moverOriginX = positionX
        self.positionY = positionY
        self.moverSpeed = -speed

    def addMover(self, moverImageSource):
        moverImage = pyglet.image.load(moverImageSource)
        moverSpacingX = len(self.movers) * self.moverWidth + 1
        moverX = self.moverOriginX + moverSpacingX
        moverY = self.positionY
        moverSprite = pyglet.sprite.Sprite(img=moverImage, x=moverSpacingX, y=moverY, batch=self.batch, group=self.group)
        mover = Mover(moverX, moverY, moverSprite)
        self.movers.append(mover)
    
    def update(self, modifier=1): 
        for mover in self.movers:
            mover.move(self.moverSpeed * modifier, 0)

            if mover.x + self.moverWidth < -self.dim.w:
                furthestMover = max(self.movers, key=lambda mover: mover.x)
                mover.x = int(furthestMover.x + self.moverWidth) - 1
            
            mover.update()

