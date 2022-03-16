
#1D
#a=[1,2.1,3.5]
#na=[]
#for ii in a:
#    na.append(ii*2)
#print(na)
    
#2D
#a=[[1,2.1,3.5],[4,5,6],[3.2,2.0,-1.2],[-0.2,-1.4,3.0]]
#mm=0
#for ii in a[mm]:
#    print(mm)
#    print(a[mm])
#    mm = mm+1

#2D*2
a=[[1,2.1,3.5],[4,5,6],[3.2,2.0,-1.2],[-0.2,-1.4,3.0]]
na=[]
mm=0
for ii in range(len(a)):
    na.append([])
    for jj in a[ii]:
        na[mm].append(jj*2)
    mm=mm+1
print(na) 

#2D dot matrix
a=[[1,0,0,0],[0,1,0,0]]
b=[[1,2.1,3.5],[4,5,6],[3.2,2.0,-1.2],[-0.2,-1.4,3.0]]
#na=a*b
#na[ii][jj]=a[ii][0]*b[0][jj]+a[ii][1]*b[1][jj]+a[ii][2]*b[2][jj]+a[ii][3]*b[3][jj]

na=[]
row_a=len(a)
col_b=len(b[0])
na=[[0]*col_b for ii in range(row_a)]
print(na)

for ii in range(len(a)):
    na.append([])
    for jj in range(len(b[0])):
        na[ii][jj]=0
        for kk in range(len(a[0])):
            na[ii][jj]=na[ii][jj]+a[ii][kk]*b[kk][jj]
        print(na[ii][jj],end=" ")
    print("\n")

