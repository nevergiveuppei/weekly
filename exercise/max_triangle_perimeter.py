
#Find out three elements from this array that form a triangle of the maximum perimeter.

a=[10,4,3,5,2]

mm=0
sol=[]
tri=[]

for ii in range(len(a)):
    for jj in range(ii+1,len(a)): 
        for kk in range(jj+1,len(a)):
            max_v=max(a[ii],a[jj],a[kk])
            perimeter=a[ii]+a[jj]+a[kk]
            dif=perimeter-2*max_v
            if dif>0:
                sol.append([])
                sol[mm].append(perimeter)
                tri.append([])
                tri[mm].append(a[ii])
                tri[mm].append(a[jj])
                tri[mm].append(a[kk])
                print(a[ii],a[jj],a[kk],"perimeter=",perimeter, end="\n")
                mm=mm+1
print(sol)
print(tri)

ans=0            
for idx, ll in enumerate(sol):
    if (ans == 0 or ll>ans):
        ans=ll
        max_idx=idx
print('Maximum value:', ans)
print(tri[max_idx])

               

             
                