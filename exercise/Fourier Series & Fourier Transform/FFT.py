
# Purpose: 
# 1: Sample a time domain input signal.
# 2: Transfrom the input signal from time domain to frequency domain through FFT(Fast Fourier Transform).
# 3: Reconstruct the frequency domain signal into time domain signal through iFFT(Inverse FFT).

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft

# --------------
# def: generate a input signal 
# --------------
def generate_sinusoid(A,f0,fs,end_t,phi):
    Ts = 1/fs
    #n = np.arange(N) # [0,1,...,N-1]
    t = np.arange(0,end_t,Ts) # t = n*Ts, t is in the unit of second
    y = A * np.sin( 2*np.pi*f0*t + phi )
    return t,y

# Generate input signal 
A   = 1   # amplitude
f0  = 5   # raw signal frequency
fs  = 150 # sampling frequency
end_t = 1 
phi = 0     # pase shift

(t,y) = generate_sinusoid(A,f0,fs,end_t,phi)

plt.figure( 1 )

plt.subplot(311)
plt.plot(t,y)
plt.xlabel("Time", size = 10,)
plt.ylabel("Amplitude", size = 10)
plt.title("Sampled signal (f0=%sHz,fs=%sHz)"%(f0,fs), color='black',fontweight='bold', size = 14) 

# FFT
X = fft(y)
#N = len(X)
#n = np.arange(N)
#time = N/fs # time is the period of time in time domain
#freq = n/time # freq ranges from 0(HZ), 1(HZ), 2(HZ),...to fs=150(HZ). 

# Due to the symmetry in FFT, the sampling point is reduced from N to N/2.
N = len(y)
n = np.arange(int(N//2))
time = N/fs
freq = n/time

plt.subplot(312)
plt.plot(freq, np.abs(X[:N//2]), 'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Amp(freq)|')
plt.title("FFT Signal", color='black',fontweight='bold', size = 14)

# Inverse FFT

Y = ifft(X)

plt.subplot(313)
plt.plot(t, Y)
plt.xlabel("Time", size = 10,)
plt.ylabel("Amplitude", size = 10)
plt.title("Reconstructed signal (f0=%sHz,fs=%sHz)"%(f0,fs), color='black',fontweight='bold', size = 14) 

plt.tight_layout() 
plt.show()