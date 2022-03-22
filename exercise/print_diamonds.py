
#print a diamond: solid or hollow

import sys
sys.argv.pop(0)
s_oddmax=0
h_oddmax=0

#########################################
#print("   *")
#print(" ",3*"*")
#print("",5*"*")
#print(7*"*")
#print("",5*"*")
#print(" ",3*"*")
#print("   *")

###############use argv to choose a solid or hollow diamond###################
while len(sys.argv)>0:
    if sys.argv[0] == '-help':
        print("-s num : num is odd, even wil fail")
        print("-h num : num is odd, even wil fail")
        sys.exit(0)
    elif sys.argv[0] == '-s':
        s_oddmax=sys.argv[1]
        print("s_oddmax=", sys.argv[1])
        sys.argv.pop(1)
    elif sys.argv[0] == '-h':
        h_oddmax=sys.argv[1]
        print("h_oddmax=", sys.argv[1])
        sys.argv.pop(1)
    sys.argv.pop(0)

###############a solid diamond###################
s_oddmax=int(s_oddmax)
if s_oddmax>0:
    print((((s_oddmax+1)//2)-1)*' '+'*')
    for kk in range(1,(s_oddmax-1),2):
        print(((s_oddmax-2-kk)//2)*' '+(kk+2)*'*')
    for kk in range(s_oddmax-4,0,-2):
        print(((s_oddmax-2-kk)//2)*' '+(kk+2)*'*')
    if s_oddmax>1:
        print((((s_oddmax+1)//2)-1)*' '+'*')
    
###############a hollow diamond###################
h_oddmax=int(h_oddmax)
if h_oddmax>0:
    print((((h_oddmax+1)//2)-1)*' '+'*')
    for kk in range(1,(h_oddmax-1),2):
        print(((h_oddmax-2-kk)//2)*' '+'*'+kk*' '+'*')
    for kk in range(h_oddmax-4,0,-2):
        print(((h_oddmax-2-kk)//2)*' '+'*'+kk*' '+'*')
    if h_oddmax>1:
        print((((h_oddmax+1)//2)-1)*' '+'*')



