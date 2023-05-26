import pyglet
from pyglet.gl import *
from pyglet.math import Mat4
from AudioSource import AudioSource
from GameManager import GameManager
from GameEventDispatcher import GameEventDispatcher

window = pyglet.window.Window(1920, 1080)

projection = Mat4.orthogonal_projection(-window.width/2, window.width/2, -window.height/2, window.height/2, z_near=-255, z_far=255)
pyglet.gl.glClearColor(1, 0.75, 0.5, 1)

gameManager = GameManager(window)
gameEvents = GameEventDispatcher(gameManager)
GameEventDispatcher.register_event_type('on_collision')
GameEventDispatcher.register_event_type('on_score')
#background = pyglet.image.load("./assets/background.jpg")
moveUp = False
moveDown = False

@gameEvents.event
def on_collision():
    pass
    #gameManager.endGame()   

@gameEvents.event
def on_score():
    gameManager.increaseScore()     

@window.event
def on_draw():
    window.projection = projection
    window.clear()
    #background.blit(-window.width/2, -window.height/2, width=window.width, height=window.height)
    gameManager.draw()

@window.event
def on_key_press(symbol, modifiers):
    global moveUp
    global moveDown
    if symbol == 32:
        gameManager.reset()
    elif symbol == 65362:
        moveUp = True
    elif symbol == 65364:
        moveDown = True
    elif symbol == 108:
        gameManager.laserCannonManager.start_laser()
    else:
        print(f"symbol: {symbol}")
@window.event
def on_key_release(symbol, modifiers):
    global moveUp
    global moveDown
    if symbol == 65362:
        moveUp = False    
    elif symbol == 65364:
        moveDown = False
        
@window.event
def on_close():
    audioSource.stop()
    pyglet.clock.unschedule(update)
    pyglet.app.exit()

def update(dt):
    gameManager.update(dt, audioSource.pitch, audioSource.db_level)
    if not gameManager.gameOver:
        gameEvents.detectCollision()
        gameEvents.detectScore()
    gameEvents.doParticlePhysics(dt)

    if moveUp:
        gameManager.playerManager.movePlayer(150*dt, -1)
    elif moveDown:
        gameManager.playerManager.movePlayer(-150*dt, 1)

audioSource = AudioSource()
audioSource.start()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()

