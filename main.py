import pyglet
from pyglet.gl import *
from pyglet.math import Mat4
from AudioSource import AudioSource
from GameManager import GameManager
from GameEventDispatcher import GameEventDispatcher
from LiveSource import LiveSource
from LiveEventQueue import LiveEventQueue

window = pyglet.window.Window(1920, 1080)

projection = Mat4.orthogonal_projection(-window.width/2, window.width/2, -window.height/2, window.height/2, z_near=-255, z_far=255)
pyglet.gl.glClearColor(115/255, 191/255, 230/255, 1)
#pyglet.gl.glClearColor(0.32, 0.91, 0.97, 1)

gameManager = GameManager(window)
gameEvents = GameEventDispatcher(gameManager)
GameEventDispatcher.register_event_type('on_collision')
GameEventDispatcher.register_event_type('on_score')
backgroundSky = pyglet.image.load("./assets/BGSky.png")


#bghSprite.scale = window.width / bghSprite.width
moveUp = False
moveDown = False




@gameEvents.event
def on_collision():

    gameManager.endGame()   

@gameEvents.event
def on_score():
    gameManager.increaseScore()     

@window.event
def on_draw():
    window.projection = projection
    window.clear()
    #backgroundSky.blit(-window.width/2, -window.height/2, width=window.width, height=window.height)
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
        gameManager.startLaser()
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
    #liveSource.stop()
    pyglet.clock.unschedule(update)
    pyglet.app.exit()

def update(dt):
    
    if moveUp:
        gameManager.playerManager.movePlayer(150*dt, -1)
    elif moveDown:
        gameManager.playerManager.movePlayer(-150*dt, 1)

        
    gameManager.update(dt, audioSource.pitch, audioSource.db_level)
    if not gameManager.gameOver:
        gameEvents.detectCollision()
        gameEvents.detectScore()
    gameEvents.doParticlePhysics(dt)

    
    #if not liveEventQueue.is_empty():
    #    event = liveEventQueue.pop()
    #    print(f"EVENT: {event.diamonds}")
        
    #bghSprite.update(bghSprite.x - 0.4)
    #bghSprite2.update(bghSprite2.x - 0.2)

audioSource = AudioSource()
audioSource.start()

#liveEventQueue = LiveEventQueue()
#liveSource = LiveSource("@ad.nah", liveEventQueue)
#liveSource.start()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()

