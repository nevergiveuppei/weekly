
##use def to compute n!

def factorial(n):
    jj=1
    for ii in range(1,n+1,1):
        jj=jj*ii
    return jj
    #print("n!=",jj)
    
print("enter an integer:", end="")
nn=int(input())
ans=factorial(nn)
print("n!=",ans)


##use Recursion to compute n!

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1)*n

print("enter an integer:", end="")
nn=int(input())
ans=factorial(nn)
print("n!=",ans)


