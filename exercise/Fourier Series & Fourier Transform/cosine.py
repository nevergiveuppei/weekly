
# Purpose: Verify the orthogonality in the bases of cos(2*n*pi*x/L) 

import math
import matplotlib.pyplot as plt

#define a cos_matrix
# define the period of cos()
print("choose a integer as period-L: ",end="")
ll=int(input())
# define the number of x point in a period-L
print("choose a float number as x_step: ",end="")
step=float(input())
# define the number of cos() bases with different frequencies
print("choose an non-zero integer for max_cos frequency: ",end="")
nn=int(input())

def basis_m(ll,nn,step):
    row=int((ll//step)+1)
    col=nn
    bm=[[0]*col for numbers in range(row)]
    for ii in range(row):
        for jj in range(nn):
            theta=(2*jj*(np.pi)*(step*(ii)))/ll
            bm[ii][jj]=math.cos(theta)
    return bm

basis_cos=basis_m(ll,nn,step)

#define the transpose matrix of a cos_matrix
def trans_m(matrix):
    row=len(matrix)
    col=len(matrix[0])
    t_matrix=[[0]*row for numbers in range(col)]
    for ii in range (col):
        for jj in range (row):
            t_matrix[ii][jj]=matrix[jj][ii]
    return t_matrix

tbasis_cos=trans_m(basis_cos)

#calculate the integral of a cos()*cos() over a period L (from x=0 to x=l)
def integral(t_mm,mm,step,ll):
    row=len(t_mm)
    col=len(mm[0])
    intgral_m=[[0]*col for numbers in range(row)]
    # consider if n=m=0
    for ii in range(len(t_mm)):
        for jj in range(len(mm[0])):
            for kk in range (len(t_mm[0])):
                intgral_m[ii][jj]=intgral_m[ii][jj]+t_mm[ii][kk]*mm[kk][jj]
            if ii==0 and jj==0:
                intgral_m[ii][jj]=intgral_m[ii][jj]*(step)/(ll)
            else:
                intgral_m[ii][jj]=intgral_m[ii][jj]*(step)/(0.5*ll)
    return intgral_m

integral_m=integral(tbasis_cos,basis_cos,step,ll)

#Check if the integral of cos()*cos() equals to an identity matrix or not
offset=0.0001

count=0
flag=1
for ii in range(len(integral_m)):
    count=count+1
    if abs(integral_m[ii][ii]-1) < offset:
        continue
    elif abs(integral_m[ii][ii]-1) > offset:
        flag=0
        break
print("diag-count=",count)
        
if flag==1:
    print("all pass in diagonal elements")
else:
    print("error in diagonal elements")


flag_2=1
for ii in range(len(integral_m)):
    for jj in range(len(integral_m[0])):
        if ii != jj and abs(integral_m[ii][jj]-0) < offset:
            continue
        elif ii != jj and abs(integral_m[ii][jj]-0) > offset:
            flag_2=0
            break
        
if flag_2==1:
    print("all pass in off-diagonal elements")
else:
    print("error in off-diagonal elements")

    











