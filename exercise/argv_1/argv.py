

import sys
print(sys.argv)

if len(sys.argv)>=2 and sys.argv[1] =='-help':
    print("please use -r readfilename.txt -w writefilename.txt")
    sys.exit()
    
if len(sys.argv)>=2 and sys.argv[1] =='-r':
    readfile = sys.argv[2]
    print("readfile =", readfile)  
    
if len(sys.argv)>=2 and sys.argv[3] =='-w':
    writefile = sys.argv[4]
    print("writefile =", writefile)  
    
#define read file function
def read_matrix(readfile):
    fp   = open(readfile, "r")
    line = fp.readline()
    mtx  = []   
    mm = 0 
    while line :
        mtx.append([])
        str_list = line.split()
        for ii in str_list:
            jj = float(ii)
            mtx[mm].append(jj)
        mm = mm+1
        line = fp.readline()
    return mtx

rmatrix=read_matrix(readfile)
print("readfile=", readfile)
print("readmatrix=", rmatrix)

#define & open write file 
fout = open(writefile, "w")
def write_matrix(rmitrix):
    for ii in rmitrix:
        for jj in ii:
            fout.write("%f"%jj)
        fout.write("\n")
    return
    
wmatrix=write_matrix(rmatrix)
print("writefile:", writefile)
print("writematrix=", rmatrix)






