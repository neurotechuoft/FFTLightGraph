import numpy as np
#from scipy.fftpack import fft
#from scipy.fftpack import fftfreq
import numpy.fft as fft
#import matplotlib.pyplot as plt
import math

def time_to_frequency(data):
    Fs = 128.0 # sampling frequency
    Ts = 1.0/Fs # period
    t = np.arange(len(data)) / Fs # time axis for plotting

    n = len(data) # length of the signal
    #print "n: ", n
    #print "Ts: ", Ts
    #print "t: ", t
    k = np.arange(n)
    T = n/Fs # total time sampling
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))]

    Y = np.fft.fft(data)/n
    Y = Y[range(int(n/2))]
    print 20*np.log10(abs(Y))
    return 20*np.log10(abs(Y))
    #fig, ax = plt.subplots(2, 1)
    #ax[0].plot(t,data)
    #ax[0].set_xlabel('Time')
    #ax[0].set_ylabel('Voltage')
    #ax[1].plot(frq,20*np.log10(abs(Y)),'r')
    #ax[1].set_xlabel('Freq (Hz)')

    #plt.draw()
    #plt.show()
if __name__ == '__main__':
    data = [1, 4, 5, 7, 4, 5]
    time_to_frequency(data)
