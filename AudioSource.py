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

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

"""
import threading
import pyaudio
import numpy as np

class AudioSource(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.chunk_size = 512
        self.format = pyaudio.paFloat32
        self.channels = 1
        self.rate = 48000
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






class AudioSource(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.chunk_size = 1024
        self.rate = 48000
        self.threshold = 0.1
        self.alpha = 0.5
        self.previous_pitch = 0
        self.pitch = 0
        self.db_level = 0
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk_size)
    def run(self):
        while True:
            try:
                data = np.fromstring(self.stream.read(self.chunk_size), dtype=np.float32)
                autocorr = np.correlate(data, data, mode='full')
                autocorr = autocorr[len(autocorr)//2:]
                autocorr /= np.max(autocorr)  # Normalize autocorrelation
                autocorr_diff = np.diff(autocorr)
                zero_crossings = np.where(np.diff(np.sign(autocorr_diff)))[0]

                if len(zero_crossings) > 0:
                    pitch_period = zero_crossings[0]
                    pitch_hz = self.rate / pitch_period
                    self.pitch = self.alpha * pitch_hz + (1 - self.alpha) * self.previous_pitch
                    self.previous_pitch = self.pitch
                else:
                    self.pitch = 0

                # Compute the dB level
                rms = np.sqrt(np.mean(np.square(data)))
                self.db_level = 20 * np.log10(rms)

            except Exception as e:
                print(f"Error: {e}")
            
    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()                
"""