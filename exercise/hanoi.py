

###############################Version_1
#Tower of Hanoi
# n: the number of disks
# pa: pillar a
# pb: pillar b
# pc: pillar c
# a: the number of disks on pa
# b: the number of disks on pb
# c: the number of disks on pc

#n=int(input("enter the number of disk="))
#aa = list(range(1,n+1,1))
#bb = []
#cc = []
#print("initial condition:")
#print("A =",aa)
#print("B =",bb)
#print("C =",cc)

#def hanoi(n,pa,pb,pc,a,b,c):
#    if n==1:
#        print("move one disk from",pa,"to",pc)
#        c.insert(0,a[0])
#        a.pop(0)
#        print(pa," = ",a)
#        print(pb," = ",b)
#        print(pc," = ",c)
#        
#    else:
#        hanoi(n-1,pa,pc,pb,a,c,b)
#        hanoi(1,pa,pb,pc,a,b,c)
#        hanoi(n-1,pb,pa,pc,b,a,c)
#        
#hanoi(n,"A","B","C",aa,bb,cc)

###############################Version_2 (use sort.() to print A,B,C in order)
#n=int(input("enter the number of disk="))
#aa = list(range(1,n+1,1))
#bb = []
#cc = []
#print("initial condition:")
#print("A =",aa)
#print("B =",bb)
#print("C =",cc)

#def firstElement(element):
#    return element[0]
#
#def hanoi(n,pa,pb,pc,a,b,c):
#    if n==1:
#        print("move one disk from",pa,"to",pc)
#        c.insert(0,a[0])
#        a.pop(0)
#        ll=[(pa,"=",a),(pb,"=",b),(pc,"=",c)]
#        ll.sort(key=firstElement)
#        print(" ".join('%s' %id for id in ll[0]))
#        print(" ".join('%s' %id for id in ll[1]))
#        print(" ".join('%s' %id for id in ll[2]))
#    else:
#        hanoi(n-1,pa,pc,pb,a,c,b)
#        hanoi(1,pa,pb,pc,a,b,c)
#        hanoi(n-1,pb,pa,pc,b,a,c)
#        
#hanoi(n,"A","B","C",aa,bb,cc)

###############################Version_3 (creat a txt.file and write messages on the txt.file)

#n=int(input("enter the number of disk="))
#aa = list(range(1,n+1,1))
#bb = []
#cc = []
#print("initial condition:")
#print("A =",aa)
#print("B =",bb)
#print("C =",cc)
#
#w_file = open('/home/WuShe/hanoi.txt',"w+")  ##create a txt.file
#
#def firstElement(element):
#    return element[0]
#
#def hanoi(n,pa,pb,pc,a,b,c):
#    if n==1:
#        print("move one disk from",pa,"to",pc)
#        m1=["move one disk from",pa,"to",pc]
#        w_file.write(" ".join('%s' %id for id in m1))   ##write operation message
#        w_file.write("\n")
#        c.insert(0,a[0])
#        a.pop(0)
#        ll=[(pa,"=",a,"\n"),(pb,"=",b,"\n"),(pc,"=",c,"\n")]
#        ll.sort(key=firstElement)
#        print(" ".join('%s' %id for id in ll[0]))
#        print(" ".join('%s' %id for id in ll[1]))
#        print(" ".join('%s' %id for id in ll[2]))
#        w_file.write(" ".join('%s' %id for id in ll[0]))   ##write 
#        w_file.write(" ".join('%s' %id for id in ll[1]))   ##write 
#        w_file.write(" ".join('%s' %id for id in ll[2]))   ##write 
#    else:
#        hanoi(n-1,pa,pc,pb,a,c,b)
#        hanoi(1,pa,pb,pc,a,b,c)
#        hanoi(n-1,pb,pa,pc,b,a,c)
#        
#hanoi(n,"A","B","C",aa,bb,cc)
#
#w_file.close()

###############################Version_4 (use Dictionary and creat/write a txt.file )

w_file = open('/home/WuShe/hanoi.txt',"w+")  ##create a txt.file

n=int(input("enter the number of disk="))
print("initial condition:")
w_file.write("initial condition:"+"\n")

dic = {} 
dic['A'] = list(range(1,n+1,1))
dic['B'] = []
dic['C'] = []
print(dic)
w_file.write(str(dic)+"\n")

def hanoi(n,pa,pb,pc):
    if n==1:
        print("move one disk from",pa,"to",pc)
        m1="move one disk from "+pa+" to "+pc+"\n"
        w_file.write(m1)
        dic[pc].insert(0,dic[pa][0])
        dic[pa].pop(0)
        print(dic)
        w_file.write(str(dic)+"\n")   ##write 
    else:
        hanoi(n-1,pa,pc,pb)
        hanoi(1,pa,pb,pc)
        hanoi(n-1,pb,pa,pc)
        
hanoi(n,"A","B","C")
w_file.close()

###############################Verification Code(use this code to verify if the hanoi.py operates correctly or not)
import re
print("start to verify")

r_file = open('/home/WuShe/hanoi.txt',"r")

def read(file):
    line = file.readline()
    dic = {} 
    dic['A'] = list(range(1,n+1,1))
    dic['B'] = []
    dic['C'] = []
    print("initial condition=","/n",dic)
    while line:
        mth = re.search(r'from ([ABC]) to ([ABC])',line)
        if mth:
            print("str is matched, %s, %s "%(mth.group(1), mth.group(2)))
            dic[mth.group(2)].insert(0,dic[mth.group(1)][0])
            dic[mth.group(1)].pop(0)
            print(dic)
        #else:
            #print("str is not matched")
        line = file.readline()

vef=read(r_file)

r_file.close()




