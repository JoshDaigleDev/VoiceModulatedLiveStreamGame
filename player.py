import pyglet
from pyglet.gl import *

class Player:
    def __init__(self, x, y, radius=50):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        circle = pyglet.shapes.Circle(self.x, self.y, self.radius, color=(255, 0, 0))
        circle.draw()

    def move(self, dy):
        self.y += dy