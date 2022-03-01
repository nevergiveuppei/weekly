#印出九九乘法表

for i in range(1,10):
    for j in range(1,10):
        k=i*j
        #For數字對齊需求
        if i*j<10:
            print("%d*%d=%d"%(i,j,k),end='  ')
        else:
            print("%d*%d=%d"%(i,j,k),end=' ')
    print('')    
    
