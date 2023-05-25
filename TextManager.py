import pyglet
from pyglet import font
class TextManager():
    
    def __init__(self, window):
        self.window = window

        font.add_file('./assets/Perfect DOS VGA 437 Win.ttf')
        self.eightBitFont = font.load('Perfect DOS VGA 437 Win', 64)
        self.label = pyglet.text.Label('0',
                          font_name=self.eightBitFont.name,
                          font_size=self.eightBitFont.size,
                          x=0, y=window.height/2-window.height/8)

    def draw(self):
        self.label.draw()

    def update(self, score):
        self.label.text = f"SCORE: {score}"