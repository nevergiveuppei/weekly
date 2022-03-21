
import sys, numpy
print(sys.argv)
sys.argv.pop(0)

readfile=set()
input1=set()
input2=set()
writefile=set()

while len(sys.argv)>0:
    if sys.argv[0] == '-help':
        print("-r readfile.txt -mul input1.txt input2.txt -w writefile.txt")
        sys.exit(0)
    elif sys.argv[0] == '-r':
        readfile=sys.argv[1]
        print("readfile=", sys.argv[1])
        sys.argv.pop(1)
    elif sys.argv[0] == '-mul':
        input1=sys.argv[1]
        input2=sys.argv[2]
        print("input1=", sys.argv[1])
        print("input2=", sys.argv[2])
        sys.argv.pop(1)
        sys.argv.pop(1)
    elif sys.argv[0] == '-w':
        writefile=sys.argv[1]
        print("writefile=", sys.argv[1])
        sys.argv.pop(1)
    sys.argv.pop(0)

##########################Define read file function###############################
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

if len(readfile)>0:
    rmatrix=read_matrix(readfile)
    print("readfile=", readfile)
    print("readmatrix=", rmatrix)

if len(input1)>0:
    a_matrix=read_matrix(input1)
    print("a_matrix=", a_matrix)

if len(input1)>0:
    b_matrix=read_matrix(input2)
    print("b_matrix=", b_matrix)

##########################Define write file  function###############################

fout = open(writefile, "w")
def write_matrix(rmitrix):
    for ii in rmitrix:
        for jj in ii:
            fout.write("%.2f "%jj)
        fout.write("\n")
    return

if len(readfile)>0:
    wmatrix=write_matrix(rmatrix)

if len(input1)>0:
    write_matrix(a_matrix)

if len(input2)>0:
    write_matrix(b_matrix)
    
##########################Define mul_matrix function###############################

if len(input1)>0 and len(input2)>0:
        na=[]
        row_a=len(a_matrix)
        col_b=len(b_matrix[0])
        na=[[0]*col_b for ii in range(row_a)]
        print(na)    
        for ii in range(len(a_matrix)):
#           na.append([])
            for jj in range(len(b_matrix[0])):
#               na[ii][jj]=0
                for kk in range(len(a_matrix[0])):
                    na[ii][jj]=na[ii][jj]+a_matrix[ii][kk]*b_matrix[kk][jj]
#               print(na[ii][jj],end=" ")
#           print("")
        print(na)
        write_matrix(na)
