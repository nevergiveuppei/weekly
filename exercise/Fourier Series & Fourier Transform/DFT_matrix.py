
# Purpose: prove the DFT(Discrete Fourier Transform) matrix is orthonormal, i.e., np.dot(hermitian_DFT*DFT_m)=identity matrix

import numpy as np


# define the variables ####################################
print("choose a integer as period-L: ",end="")
ll=int(input())

j = complex(0,1)  
c_zero = complex(0,0)  
c_one = complex(1,0) 

#define the index in DFT matrix ###########################
index_m=np.zeros((ll,ll),dtype=complex)
for xx in range (ll):
    for nn in range (ll):
        index_m[xx][nn]= -(j*2*(np.pi)/ll)*xx*nn
#print(index_m)

#define the DFT matrix ###########################
DFT_m=np.zeros((ll,ll),dtype=complex)
DFT_m=np.exp(index_m)

for ii in range(ll):
    for jj in range(ll):
        DFT_m[ii][jj]=DFT_m[ii][jj]*(ll)**(-0.5)

#print(DFT_m)

#find the Hermitian matrix of DFT_m
trans_DFT=np.zeros((ll,ll),dtype=complex)
trans_DFT=np.transpose(DFT_m)

hermitian_DFT=np.zeros((ll,ll),dtype=complex)
for ii in range(ll):
    for jj in range(ll):
        hermitian_DFT[ii][jj]=np.conjugate(trans_DFT[ii][jj])
        
# check if trans_DFT * DFT_m equals to an identity matrix.
inner_dot=np.dot(hermitian_DFT,DFT_m)
print(inner_dot)

# check diagonal terms
offset=0.0001
flag=1

for ii in range (ll):
    if abs(inner_dot[ii][ii]-c_one) < offset:
        continue
    elif abs(inner_dot[ii][ii]-c_one) > offset:
        flag=0
        break
        
if flag==1:
    print("all pass in diagonal terms")
else:
    print("error in diagonal terms")

# check off-diagonal terms
flag_2=1
for ii in range (ll):
    for jj in range(ll):
        if ii != jj and abs(inner_dot[ii][jj]-c_zero) < offset:
                continue
        elif ii != jj and abs(inner_dot[ii][jj]-c_zero) > offset:
            flag_2=0
            break
        
if flag_2==1:
    print("all pass in off-diagonal terms")
else:
    print("error in off-diagonal terms")




