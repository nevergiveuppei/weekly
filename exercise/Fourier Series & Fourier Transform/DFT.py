
# Purpose: 
# 1: Sample a time domain input signal.
# 2: Transfrom the input signal from time domain to frequency domain through DFT(Discrete Fourier Transform).
# 3: Reconstruct the frequency domain signal to time domain signal through iDFT(Inverse DFT).

import numpy as np
import matplotlib.pyplot as plt
import FFT 


# --------------
# def: DFT matrix 
# --------------
def DFT_matrix(N,j):
    index_m=np.zeros((N,N),dtype=complex)
    for kk in range (N):
        for nn in range (N):
            index_m[kk][nn]= -(j*2*(np.pi)/N)*kk*nn   
    DFT_m=np.zeros((N,N),dtype=complex)
    DFT_m=np.exp(index_m)
    for ii in range(N):
        for jj in range(N):
            DFT_m[ii][jj]=DFT_m[ii][jj]*(N)**(-0.5)
    return DFT_m

# --------------
# def: DFT transform 
# --------------
def DFT_transform(dft,signal_t):
    DFT_t=np.dot(dft,signal_t)
    return DFT_t 

# --------------
# def: inverse DFT matrix 
# --------------
def iDFT_matrix(N,j):
    index_m=np.zeros((N,N),dtype=complex)
    for kk in range (N):
        for nn in range (N):
            index_m[kk][nn]= (j*2*(np.pi)/N)*kk*nn   
    iDFT_m=np.zeros((N,N),dtype=complex)
    iDFT_m=np.exp(index_m)
    for ii in range(N):
        for jj in range(N):
            iDFT_m[ii][jj]=iDFT_m[ii][jj]*(N)**(-0.5)
    return iDFT_m

#def iDFT_matrix(DFT_m):
#    trans_DFT=np.zeros((N,N),dtype=complex)
#    trans_DFT=np.transpose(DFT_m)
#    iDFT_m=np.zeros((N,N),dtype=complex)
#    for ii in range(N):
#        for jj in range(N):
#            iDFT_m[ii][jj]=np.conjugate(trans_DFT[ii][jj])
#    return iDFT_m  
     
# --------------
# def: inverse-DFT transform 
# --------------
def iDFT_transform(idft,signal_f):
    iDFT_t=np.dot(idft,signal_f)
    return iDFT_t 


################################################################
#   Main Code
################################################################

# Generate input signal 
A   = 1   # amplitude
f0  = 5   # raw signal frequency
fs  = 150 # sampling frequency
end_t = 1 
phi = 0     # pase shift

(t,y)=FFT.generate_sinusoid(A,f0,fs,end_t,phi)  # import the def: generate_sinusoid() from FFT.py


# DFT transform
j = complex(0,1)
N=len(y)
DFT_m=DFT_matrix(N,j) 
DFT=DFT_transform(DFT_m,y)

n = np.arange(int(N//2))
time = N/fs
freq = n/time

# inverse DFT transform
j = complex(0,1)
N=len(y)
iDFT_m=iDFT_matrix(N,j)
iDFT=iDFT_transform(iDFT_m,DFT)


# Plot 
plt.figure( 1 )

plt.subplot(311)
plt.plot(t,y)
plt.xlabel("Time", size = 10,)
plt.ylabel("Amplitude", size = 10)
plt.title("Sampled signal (f0=%sHz,fs=%sHz)"%(f0,fs), color='black',fontweight='bold', size = 14) 
  
plt.subplot(312)
plt.plot(freq,np.abs(DFT[:N//2]),'r-')
plt.xlabel('freq (Hz)')
plt.ylabel('|Amp(freq)|')
plt.title("DFT signal", color='black',fontweight='bold', size = 14)

plt.subplot(313)
plt.plot(t,iDFT)
plt.xlabel("Time", size = 10,)
plt.ylabel("Amplitude", size = 10)
plt.title("Reconstructed signal (f0=%sHz,fs=%sHz)"%(f0,fs), color='black',fontweight='bold', size = 14) 

plt.tight_layout() 
plt.show()
