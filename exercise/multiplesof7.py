#辨別輸入數字是否為7的倍數

# try-except
#i=input("enter a number:")
#try: 
#   i = int(i)
#   print(isinstance(i,int))
#except:
#   print("err type")


#start

i=input("enter a number: ")
# try-except is for wrong input data type  
try:
    i=int(i)
    if i%7==0:
        print("the input is a multiple of 7")
    else:
        print("the input is not a multiple of 7")
except:
    print("error type")

#end
