import pyglet
from pyglet.gl import *
from pyglet.math import Mat4
from AudioSource import AudioSource
from GameManager import GameManager

window = pyglet.window.Window(1920, 1080)
projection = Mat4.orthogonal_projection(-window.width/2, window.width/2, -window.height/2, window.height/2, z_near=-255, z_far=255)
pyglet.gl.glClearColor(1, 0.7, 0.75, 1)

gameManager = GameManager(window)

@window.event
def on_draw():
    window.projection = projection
    gameManager.draw()

def update(dt):
    pitch = audioSource.pitch
    decibles = audioSource.db_level
    gameManager.update(dt, pitch, decibles)

audioSource = AudioSource()
audioSource.start()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
