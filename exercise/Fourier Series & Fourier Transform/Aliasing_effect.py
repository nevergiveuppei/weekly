
# Purpose: 
# 1: Sample a time domain input signal with multiple frequencies
# 2: Transfrom the input signal from time domain to frequency domain through FFT(Fast Fourier Transform).
# 3: Observe aliasing effect under different sampling frequencies

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
import matplotlib.ticker 
from matplotlib.ticker import MultipleLocator

# --------------
# def: generate a input signal contains multiple frequencies
# --------------
def generate_sinusoid(A_1,A_2,A_3,f0_1,f0_2,f0_3,fs,end_t,phi_1,phi_2,phi_3):
    Ts = 1/fs
    #n = np.arange(N) # [0,1,...,N-1]
    t = np.arange(0,end_t,Ts) # t = n*Ts, t is in the unit of second
    y = A_1 * np.sin( 2*np.pi*f0_1*t + phi_1 ) + A_2 * np.sin( 2*np.pi*f0_2*t + phi_2 ) + A_3 * np.sin( 2*np.pi*f0_3*t + phi_3 )
    return t,y

################################################################################
#   MAIN
################################################################################

# Parameters
# input signal 
A_1   = 1
A_2   = 2
A_3   = 3   
f0_1  = 1000   # raw signal frequency
f0_2  = 4500
f0_3  = 6000
fs  = 50000 # sampling frequency
end_t = 0.002 
phi_1 = 0     # phase shift
phi_2 = 0
phi_3 = 0
# sampling frequency
fs_1  = 14000
fs_2  = 10000

##############################
# Plot input signal (time domain)
(t,y) = generate_sinusoid(A_1,A_2,A_3,f0_1,f0_2,f0_3,fs,end_t,phi_1,phi_2,phi_3)

plt.figure(figsize=(12,8))
plt.subplot(221)
plt.plot(t,y)
plt.xlabel("Time", size = 10)
plt.ylabel("Amplitude", size = 10)
plt.title("Input signal (f0=%sKHz,%sKHz,%sKHz,fs=%sKHz)"%(f0_1/1000,f0_2/1000,f0_3/1000,fs/1000), color='black',fontweight='bold', size = 10) 
plt.xlim(0, end_t)

##############################
# Plot spectrum input signal (frequency domain)
X = fft(y)
N = len(y)
X = fft(y)/N # Normalization
n = np.arange(int(N//2))
time = N/fs
freq = n/time/1000 # in the unit of KHz

ax = plt.subplot(223)

xmajorLocator = MultipleLocator(1)           #x-axis
xminorLocator = MultipleLocator(0.5) 
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_minor_locator(xminorLocator)

ymajorLocator = MultipleLocator(0.5)         #y-axis
yminorLocator = MultipleLocator(0.25) 
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major')           #grid
ax.yaxis.grid(True, which='major')

plt.stem(freq, np.abs(X[:N//2]), 'r', markerfmt=" ", basefmt="-r")
plt.xlabel('freq (KHz)')
plt.ylabel('|Amp(freq)|')
plt.title("FFT_input signal", color='black',fontweight='bold', size = 10) 
plt.xlim(0, N//2/time/1000)

############################
# Spectrum under fs=fs_1
fs  = fs_1
(t,y) = generate_sinusoid(A_1,A_2,A_3,f0_1,f0_2,f0_3,fs,end_t,phi_1,phi_2,phi_3)

N = len(y)
X = fft(y)/N # Normalization
n = np.arange(int(N//2))
time = N/fs
freq = n/time/1000 # in the unit of KHz

ax = plt.subplot(222)
#x-axis
xmajorLocator = MultipleLocator(1)
xminorLocator = MultipleLocator(0.5) 
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_minor_locator(xminorLocator)
#y-axis
ymajorLocator = MultipleLocator(0.5)
yminorLocator = MultipleLocator(0.25) 
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
#grid
ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='major')

plt.stem(freq, np.abs(X[:N//2]), 'r', markerfmt=" ", basefmt="-r")
plt.xlabel('freq (KHz)')
plt.ylabel('|Amp(freq)|')
plt.title("FFT_fs=%sKHz"%(fs/1000), color='black',fontweight='bold', size = 10) 
plt.xlim(0, N//2/time/1000)

############################
# FFT spectrum under fs=fs_2
fs  = fs_2
(t,y) = generate_sinusoid(A_1,A_2,A_3,f0_1,f0_2,f0_3,fs,end_t,phi_1,phi_2,phi_3)

N = len(y)
X = fft(y)/N # Normalization

n = np.arange(int(N//2))
time = N/fs
freq = n/time/1000 # in the unit of KHz

ax = plt.subplot(224)
#x-axis
xmajorLocator = MultipleLocator(1)
xminorLocator = MultipleLocator(0.5) 
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_minor_locator(xminorLocator)
#y-axis
ymajorLocator = MultipleLocator(0.5)
yminorLocator = MultipleLocator(0.25) 
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
#grid
ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='major')

plt.stem(freq, np.abs(X[:N//2]), 'r', markerfmt=" ", basefmt="-r")
plt.xlabel('freq (KHz)')
plt.ylabel('|Amp(freq)|')
plt.title("FFT_fs=%sKHz"%(fs/1000), color='black',fontweight='bold', size = 10) 
plt.xlim(0, N//2/time/1000)

plt.savefig("f0_1_%dHz_f0_2_%dHz_f0_2_%dHz.png"%(f0_1,f0_2,f0_3)) 
plt.tight_layout()
plt.show()