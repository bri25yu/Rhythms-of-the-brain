import numpy as np


class FFT:
    @staticmethod
    def plot(seq, ax, label):
        sp = np.fft.rfft(seq)
        freq = np.fft.rfftfreq(seq.shape[0])

        magnitude = np.abs(sp)
        magnitude[0] = 0.0

        ax.plot(freq, magnitude, label=label)
