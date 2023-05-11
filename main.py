import pyglet
from pyglet.gl import *
from player import Player
from pyglet.math import Mat4


window = pyglet.window.Window(1920, 1080)
projection = Mat4.orthogonal_projection(-window.width/2, window.width/2, -window.height/2, window.height/2, z_near=-255, z_far=255)
window.projection = projection
x, y = window.width//6, window.height//2
radius = 25

player = Player(0, 0)

speed = 50

@window.event
def on_draw():
    window.projection = projection
    window.clear()
    player.draw()


def update(dt):
    # Move the circle to the right
    player.move(speed*dt)
    # If the circle goes off the screen, wrap around to the left
    if player.y > window.height + player.radius:
        player.y = -player.radius
    

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()

