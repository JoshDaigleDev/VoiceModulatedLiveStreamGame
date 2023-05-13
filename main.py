import pyglet
from pyglet.gl import *
from player import Player
from pyglet.math import Mat4
from audio import AudioAnalyzerThread
from obsticle_coordinator import obsticle_coordinator

window = pyglet.window.Window(1920, 1080)

projection = Mat4.orthogonal_projection(-window.width/2, window.width/2, -window.height/2, window.height/2, z_near=-255, z_far=255)
window.projection = projection
x, y = -window.width//4, 0
radius = 25

player = Player(x, y)
pyglet.gl.glClearColor(1, 0.7, 0.75, 1)

speed = 50

obsticle_coordinator = obsticle_coordinator(window)

@window.event
def on_draw():
    window.projection = projection

    window.clear()
    obsticle_coordinator.draw()
    player.draw()

audio_thread = AudioAnalyzerThread()
audio_thread.start()

def map_range(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    new_value = (((value - old_min) * new_range) / old_range) + new_min
    return new_value

def adna_map(pitch):
    value = min(pitch, 600)
    value = max(pitch, 150)
    value = round(pitch)
    #print("Pitch:   ", value)

    movement = 0
    if value < 100:
        movement = 0
    elif value < 200:
        movement = -300
    elif value < 250:
        movement = -200
    elif value < 300:
        movement = -100
    elif value < 350:
        movement = 0
    elif value < 400: 
        movement = 100
    elif value < 450:
        movement = 200
    else:
        movement = 300
    
    return movement

#150 1 200 2 250 3 300 4 350 5 400 6 450 7 500 8 550 9 600

def update(dt):
    # Move the circle to the right
    pitch = audio_thread.pitch
    movement = adna_map(pitch)
    #movement = 0
    #if value > 125:
      #  movement = map_range(value, 125, 600, -300, 700)
   # print("Pitch:   ", pitch)
    #print("Movement:", movement)
        
    
    # If the circle goes off the screen, wrap around to the left
    if audio_thread.db_level > -40:
        if movement > 0 and player.y + player.radius < window.height/2:
            player.move(0, movement*dt)

        if movement < 0 and player.y - player.radius > -window.height/2:
            player.move(0, movement*dt)


    player.update()
    obsticle_coordinator.update(dt)

    

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()

