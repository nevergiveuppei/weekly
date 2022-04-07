

##calculate b to the power of n

def power(base,radix):
    ans=1
    for ii in range (1,radix+1,1):
        ans=ans*base                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    return ans

print("choose a base number:", end="")
aa=float(input())
print("choose a radix number:", end="")
bb=int(input())

ans=power(aa,bb)
print("answer=", ans)
    