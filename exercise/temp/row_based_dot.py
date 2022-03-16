

#a: 2*4
a=[[1,0,0,0],[0,1,0,0]]
#b: 4*3
b=[[1,2.1,3.5],[4,5,6],[3.2,2.0,-1.2],[-0.2,-1.4,3.0]]
#na=a*b
#na[ii][jj]=a[ii][0]*b[0][jj]+a[ii][1]*b[1][jj]+a[ii][2]*b[2][jj]+a[ii][3]*b[3][jj]

a=[[1,0,0,0],[0,1,0,0]]
b=[[1,2.1,3.5],[4,5,6],[3.2,2.0,-1.2],[-0.2,-1.4,3.0]]

na=[]
nn=0
for ii in range(len(a)):
    na.append([])
    for jj in a[ii]:     
        for kk in range(len(b)):     
        na[mm].append(jj*b[kk])
        mm=mm+1
        kk=kk+1   
    nn=nn+1
print(na) 

