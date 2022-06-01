import sounddevice as sd
import numpy as np
from matplotlib import pyplot as plt
import time

class device:
    def __init__(self, fs=44100):
        self.sd = sd
        self.sd.default.device = 0
        self.sd.default.samplerate = fs
        self.sd.default.dtype=np.float32
        self.sd.default.channels = 1
        pass

    def setAcqTime(self, dt):
        self.dt = dt
        self.samples = int(self.sd.default.samplerate*self.dt)
        pass

    def acquire(self):
        self.data = np.asarray(self.sd.rec(self.samples))
        pass


if __name__ == "__main__":
    dev = device()
    dev.setAcqTime(1.0)
    dev.acquire()
    time.sleep(1)
    plt.plot(dev.data)
    plt.show()