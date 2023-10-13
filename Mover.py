class Mover:
    def __init__(self, x, y, sprite=None):
        self.x = x
        self.y = y
        self.sprite = sprite
    
    
    def draw(self):
        self.sprite.draw()


    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    

    def update(self):
        if self.sprite:
            self.sprite.update(self.x, self.y)