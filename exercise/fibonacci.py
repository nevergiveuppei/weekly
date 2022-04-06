
#use Fibonacci sequence
#0,1,1,2,3,5,8,11,19......

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print("find the nth integer in Fibonacci sequence:", end="")
nn=int(input())
ans=fibonacci(nn)
print("fibonacci=",ans)




