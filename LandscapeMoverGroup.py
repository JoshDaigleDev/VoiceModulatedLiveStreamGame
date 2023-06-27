import pyglet 
from Mover import Mover

class LandscapeMoverGroup:

    def __init__(self, dim, imgWidth, speed, positionX, positionY):
        self.dim = dim
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
        moverSprite = pyglet.sprite.Sprite(img=moverImage, x=moverSpacingX, y=moverY)
        mover = Mover(moverX, moverY, moverSprite)
        self.movers.append(mover)
    
    def draw(self): 
        for mover in self.movers:
            mover.draw()
    
    def update(self): 
        for mover in self.movers:
            mover.move(self.moverSpeed, 0)

            if mover.x + self.moverWidth < -self.dim.w:
                furthestMover = max(self.movers, key=lambda mover: mover.x)
                mover.x = int(furthestMover.x + self.moverWidth) - 1
            
            mover.update()

