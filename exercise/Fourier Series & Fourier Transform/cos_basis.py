
#Draw cos() with matplotlib and calculate the orthogonality between cos()

import numpy as np
import math
import matplotlib.pyplot as plt

# the 1st cos frequency############################################
print("choose an non-zero integer for the 1st cos() frequency: ",end="")
nn1=int(input())

# the 2nd cos frequency############################################

print("choose an non-zero integer for the 2nd cos() frequency: ",end="")
nn2=int(input())

# the number of point in x_axis####################################
print("choose a integer as period-L: ",end="")
ll=int(input())

print("choose a float number as x_step: ",end="")
step=float(input())

fig, ax = plt.subplots(2,1)

## the 1st cos ####################################################
x_axis=[]
for xx in range(0,ll+1,1):
    x_axis.append(xx)

amp_cos=[]
for xx in range(0,ll+1,1):
    theta=(2*nn1*(np.pi)*xx)/ll
    e_cos=math.cos(theta)
    amp_cos.append(e_cos)

ax[0].plot(x_axis,amp_cos)

## the 2nd cos ####################################################

x2_axis=[]
for xx2 in range(0,ll+1,1):
    x2_axis.append(xx2)

amp2_cos=[]
for xx2 in range(0,ll+1,1):
    theta=(2*nn2*(np.pi)*xx2)/ll
    e2_cos=math.cos(theta)
    amp2_cos.append(e2_cos)

ax[1].plot(x2_axis,amp2_cos)

plt.savefig("fg_cos_nn1_%d_nn2_%d.png"%(nn1,nn2)) 
plt.show()

# compute the inner-product of two cos() functions ################

sum=0
for xx in np.arange(0,ll+1,step):
    theta1=(2*nn1*(np.pi)*xx)/ll
    e_cos=math.cos(theta1)  
    theta2=(2*nn2*(np.pi)*xx)/ll
    e2_cos=math.cos(theta2)
    sum=sum+(e_cos*e2_cos*step)/(0.5*ll)

print("inner-product=",sum)
    