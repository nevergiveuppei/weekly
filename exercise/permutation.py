
#Permutations
#數字: 1,2,3....ii，能組成幾種數字

print("enter a number=", end="")
jj=input()
ii=int(jj)

numerator=1
for kk in range(1,ii+1,1):
    numerator=kk*numerator

count=0
for step in range(0,ii,1):
    denominator=1
    for ll in range (1,ii-step,1):
        denominator=ll*denominator
    cnt=numerator//denominator
    count=count+cnt
print("count=", count)

##############math.factorial()############################

import math

print("enter a number=", end="")
jj=input()
ii=int(jj)

numerator=math.factorial(ii)

count=0
for ll in range (ii):
    denominator=math.factorial(ll)
    cnt=numerator//denominator
    count=count+cnt
print("count=", count)

##############Itertools.permutation()#####################
from itertools import permutations   

print("enter a number=", end="")
jj=input()
ii=int(jj)

count=0
for ll in range(1,ii+1,1):
    cnt=len(list(permutations(range(1,ii+1),ll)))
    count=count+cnt
print("count=",count)


