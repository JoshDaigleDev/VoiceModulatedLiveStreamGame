import pyglet
from pyglet.gl import *
from pyglet.math import Mat4
from AudioSource import AudioSource
from GameManager import GameManager
from CollisionEventDispatcher import CollisionEventDispatcher

window = pyglet.window.Window(1920, 1080)

projection = Mat4.orthogonal_projection(-window.width/2, window.width/2, -window.height/2, window.height/2, z_near=-255, z_far=255)
pyglet.gl.glClearColor(1, 0.7, 0.75, 1)

gameManager = GameManager(window)
collisionDetector = CollisionEventDispatcher(gameManager.playerManager, gameManager.obsticleManager)
CollisionEventDispatcher.register_event_type('on_collision')

background = pyglet.image.load("background.jpg")

@collisionDetector.event
def on_collision():
    gameManager.endGame()    

@window.event
def on_draw():
    window.projection = projection
    window.clear()
    background.blit(-window.width/2, -window.height/2, width=window.width, height=window.height)
    gameManager.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == 32:
        gameManager.reset()

@window.event
def on_close():
    audioSource.stop()
    pyglet.clock.unschedule(update)
    pyglet.app.exit()

def update(dt):
    gameManager.update(dt, audioSource.pitch, audioSource.db_level)
    if not gameManager.gameOver:
        collisionDetector.detectCollision()

audioSource = AudioSource()
audioSource.start()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()

