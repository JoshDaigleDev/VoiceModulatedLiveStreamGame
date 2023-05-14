import pyglet
from entity import Entity

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.radius = 50
        #self.playerAnimation = pyglet.image.load_animation('PlayerIcon.gif')
        #self.playerSprite = pyglet.sprite.Sprite(img=self.playerAnimation, x=self.x, y=self.y)
        self.playerSprite = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(125, 75, 255))


    def draw(self):
        circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(255, 0, 0))
        #print(circle)
        circle.draw()
        #self.playerSprite.draw()

        #square = pyglet.shpaes.rectangle(self.x, self.y, self.radius, self.radius, color=(55, 55, 255))
        #self.playerSprite.draw()


    #def update(self):
        #self.playerSprite.position = (self.x, self.y)


