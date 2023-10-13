import threading
import pyaudio
import numpy as np
import aubio

class AudioSource(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.chunk_size = 2048
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 48000
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format, channels=self.channels,
                                      rate=self.rate, input=True,
                                      frames_per_buffer=self.chunk_size)
        self.pitch = 0
        self.db_level = 0
        self.aubio_pitch = aubio.pitch("default", self.chunk_size, self.chunk_size // 2, self.rate)
        self.highestPitch = 550
        self.normalPitch = 290
        self.lowestPitch = 200
        self.buffer = 25
        self.speed = 75
        self.movement = -self.speed/2
        self.direction = 1
        self.sound = False


    def run(self):
        while True:
            data = np.fromstring(self.stream.read(self.chunk_size // 2), dtype=np.float32)
            pitch = self.aubio_pitch(data)[0]
            if pitch != 0:
                self.pitch = float(pitch)
            else:
                self.pitch = 0

            rms = np.sqrt(np.mean(np.square(data)))
            self.db_level = 20 * np.log10(rms)

            self.movement, self.direction, self.sound = self.pitchToMovement(self.pitch, self.db_level)


    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()


    def updateValues(self, high, normal, low):
        self.highestPitch = high
        self.normalPitch = normal
        self.lowestPitch = low
    

    def pitchToMovement(self, pitch, decibles):
        movement = -self.speed/2
        direction = 1
        sound = False

        if decibles < -35:
            return movement, direction, sound
        
        value = min(pitch, self.highestPitch)
        value = max(value, self.lowestPitch)
        value = round(value)


        if value > self.normalPitch - self.buffer and value < self.normalPitch + self.buffer:
            movement = 0
            direction = 0
            sound = True
        elif value < self.normalPitch - self.buffer: #low pitch
            if self.normalPitch - value < value - self.lowestPitch:
                movement = -self.speed
            else:
                movement = -2*self.speed
            direction = 1
            sound = True
        elif value > self.normalPitch + self.buffer:
            if self.highestPitch - value < value - self.normalPitch:
                movement = 3*self.speed
            else:
                movement = 2*self.speed
            direction = -1
            sound = True

        return movement, direction, sound

