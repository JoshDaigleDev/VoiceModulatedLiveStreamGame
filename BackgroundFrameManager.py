import pyglet
from BackgroundFrame import BackgroundFrame

class BackgroundFrameManager:

    def __init__(self, window):
        self.window = window
        self.backgroundImage = pyglet.image.load("./assets/BG.jpg")
        self.backgroundFrames = []
        self.reset()
    
    def update(self):
        for frame in self.backgroundFrames:
            frame.move(-1, 0)
            frame.update()
            if frame.x + self.window.height < -self.window.width/2:
                self.backgroundFrames.remove(frame)
                self.addFrame()

    def draw(self):
        for frame in self.backgroundFrames:
            frame.draw()
    
    def addFrame(self):
        newFrame = BackgroundFrame(-self.window.width/2 + 2 * self.window.height, -self.window.height/2, self.backgroundImage, self.window)
        self.backgroundFrames.append(newFrame)

    def reset(self):
        self.backgroundFrames = []
        startFrame1 = BackgroundFrame(-self.window.width/2, -self.window.height/2, self.backgroundImage, self.window)
        startFrame2 = BackgroundFrame(-self.window.width/2 + self.window.height, -self.window.height/2, self.backgroundImage, self.window)
        startFrame3 = BackgroundFrame(-self.window.width/2 + 2 * self.window.height, -self.window.height/2, self.backgroundImage, self.window)

        self.backgroundFrames.append(startFrame1)
        self.backgroundFrames.append(startFrame2)
        self.backgroundFrames.append(startFrame3)
