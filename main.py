import pyglet
from pyglet.gl import *
from pyglet.math import Mat4
from AudioSource import AudioSource
from LiveSource import LiveSource
from Game import Game
from GameEventDispatcher import GameEventDispatcher
from OptionLoader import OptionLoader
from EventHelpers import *
from DotDict import DotDict

#INITIALIZATION

# This is a backup incase changing dimension goes terribly wrong. 
unit = 50
dimDict = {
    "unit": unit,
    "w": unit * 20, 
    "h": unit * 10, 
    "getDimensions": lambda: (unit, unit * 20, unit * 10)
}

dim = DotDict(dimDict)

window = pyglet.window.Window(1920, 1080)
projection = Mat4.orthogonal_projection(-dim.w, dim.w, -dim.h, dim.h, z_near=-unit, z_far=unit)
pyglet.gl.glClearColor(115/255, 191/255, 230/255, 1)

mediaPlayer = pyglet.media.Player()
breakAudio = pyglet.media.load('./Assets/PlayerBreak.mp3')

batch = pyglet.graphics.Batch()
order0 = pyglet.graphics.Group(order=0)
order1 = pyglet.graphics.Group(order=1)
order2 = pyglet.graphics.Group(order=2)
order3 = pyglet.graphics.Group(order=3)
order4 = pyglet.graphics.Group(order=4)
order5 = pyglet.graphics.Group(order=5)
order6 = pyglet.graphics.Group(order=6)
order7 = pyglet.graphics.Group(order=7)
order8 = pyglet.graphics.Group(order=8)
order9 = pyglet.graphics.Group(order=9)
orderings = (order0, order1, order2, order3, order4, order5, order6, order7, order8, order9)
rendering = (batch, orderings)

OPTIONS_FILE = 'options.yaml'
options = OptionLoader(OPTIONS_FILE)

game = Game(dim, rendering, options)
gameEvents = GameEventDispatcher(game)

GameEventDispatcher.register_event_type('on_collision')
GameEventDispatcher.register_event_type('on_score')


moveUp = False
moveDown = False
paused = False

USERNAME = "@ad.nah"
audioSource = AudioSource()
liveSource = LiveSource(USERNAME)

LiveSource.register_event_type('on_tiktok_connect')
LiveSource.register_event_type('on_tiktok_like')
LiveSource.register_event_type('on_tiktok_follow')
LiveSource.register_event_type('on_tiktok_gift')
#EVENT HANDLERS

#LIVE EVENTS
@liveSource.event()
def on_tiktok_connect(data):
    game.liveManager.handleConnect()


@liveSource.event()
def on_tiktok_like(data):
    game.individualLike()
    game.liveManager.handleLike(data)


@liveSource.event()
def on_tiktok_follow(data):
    game.liveManager.handleFollow(data)


@liveSource.event()
def on_tiktok_gift(data):
    game.liveManager.handleGift(data)


#GAME EVENTS
@gameEvents.event
def on_collision():
    global mediaPlayer
    global breakAudio
    mediaPlayer.queue(breakAudio)
    if mediaPlayer.playing:
        mediaPlayer.next_source()
    mediaPlayer.play()
    
    game.endGame()   


@gameEvents.event
def on_score():
    game.increaseScore()     


#WINDOW EVENTS
@window.event
def on_draw():
    window.projection = projection
    window.clear()
    game.draw()


@window.event
def on_key_press(symbol, modifiers):
    global moveUp
    global moveDown
    global paused

    #space 
    if symbol == 65293:
        game.reset()
    
    #up
    elif symbol == 65362:
        moveUp = True
    
    #down
    elif symbol == 65364:
        moveDown = True
    
    #s
    elif symbol == 115:
        fakeGift = {"user": "shooter", "gift": "moneygun", "diamonds": 199}
        game.liveManager.handleGift(fakeGift)

    #r
    elif symbol == 114:
        game.setOptions(OPTIONS_FILE)
        audioSource.updateValues(options.highestPitch, options.normalPitch, options.lowestPitch)
    #l
    elif symbol == 108:
        fakeLike = {"user": "liker", "totalLikes": 100000}
        game.individualLike()
        game.liveManager.handleLike(fakeLike)

    #f
    elif symbol == 102:
        fakeFollow = {"user": "TheFollower27"}
        game.liveManager.handleFollow(fakeFollow)
    
    #h
    elif symbol == 104:
        fakeGift = {"user": "hardGuy", "gift": "difficult", "diamonds": 1000}
        game.liveManager.handleGift(fakeGift)
    
    #p
    elif symbol == 32:
        paused = not paused
      
    #d
    elif symbol == 100:
        fakeGift = {"user": "FakeyJakey", "gift": "Banana", "diamonds": 400}
        game.liveManager.handleGift(fakeGift)
    #\?
    else:
        print(f"symbol: {symbol}")


@window.event
def on_key_release(symbol, modifiers):
    global moveUp
    global moveDown

    #up
    if symbol == 65362:
        moveUp = False    
    #down
    elif symbol == 65364:
        moveDown = False
        

@window.event
def on_close():
    audioSource.stop()
    pyglet.clock.unschedule(update)
    pyglet.app.exit()


#MAIN UPDATE LOOP 
def update(dt):
    global paused
    global dim

    if not paused:
        #GAME UPDATES 
        game.update(dt)
        if not game.gameOver:
            gameEvents.detectCollision()
            gameEvents.detectScore()

        # MOVEMENT HANDLING: 
        global moveUp
        global moveDown
        if moveUp or moveDown:
            if moveUp:
                game.playerManager.movePlayer(dim.unit / 20, -1)
            elif moveDown:
                game.playerManager.movePlayer(-dim.unit / 20, 1)
        else:
            game.playerManager.movePlayer(audioSource.movement*dt, audioSource.direction)


def main():
    audioSource.start()
    liveSource.start()
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()


main()
