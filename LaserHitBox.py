import math
import pyglet
class LaserHitBox:
    def __init__(self, dim, x, y):
        self.dim = dim
        self.targetX = dim.w
        self.targetY = 0
        self.value = 0
        self.increment = 0.01
        self.x = x
        self.topY = y + self.dim.unit / 2
        self.botY = y - self.dim.unit / 2
        self.active = False
        self.activeTimeLimit = 2
        self.activeTimer = self.activeTimeLimit

    def update(self, fired, gameOver):
        if not gameOver:
            self.value += self.increment
            self.targetY = 7 * self.dim.unit * math.sin(self.value)
        if self.active:
            if self.activeTimer <= 0:
                self.active = False
            else:
                self.activeTimer -= 1
        
        if fired:
            self.active = True

    
    def intersectLine(self, player, x1, y1, x2, y2):
        playerX = player.x
        playerY = player.y
        radius = player.radius

        lineVector = (x2 - x1, y2 - y1)
        circleVector = (playerX - x1, playerY - y1)
        lineLenSquared = lineVector[0] ** 2 + lineVector[1] ** 2
        projection = (circleVector[0] * lineVector[0] + circleVector[1] * lineVector[1]) / lineLenSquared if lineLenSquared != 0 else 0
        closestPoint = (x1 + projection * lineVector[0],
                        y1 + projection * lineVector[1])
        distance = math.sqrt((playerX - closestPoint[0]) ** 2 + (playerY - closestPoint[1]) ** 2)
        return distance <= radius
    
    def hit(self, player):
        return self.active and (self.intersectLine(player, self.x, self.topY, self.targetX, self.targetY) or self.intersectLine(player, self.x, self.botY, self.targetX, self.targetY))