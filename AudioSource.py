import threading
import pyaudio
import numpy as np

class AudioSource(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.chunk_size = 1024
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 44100
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=self.format, channels=self.channels,
                                      rate=self.rate, input=True,
                                      frames_per_buffer=self.chunk_size)
        self.pitch = 0
        self.db_level = 0

    def run(self):
        while True:
            data = np.fromstring(self.stream.read(self.chunk_size), dtype=np.float32)
            fft = np.fft.fft(data)
            freqs = np.fft.fftfreq(len(fft))
            index = np.argmax(np.abs(fft))
            freq = freqs[index] * self.rate
            self.pitch = abs(freq)

            rms = np.sqrt(np.mean(np.square(data)))
            self.db_level = 20 * np.log10(rms)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()