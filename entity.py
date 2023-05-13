class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Cant")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy