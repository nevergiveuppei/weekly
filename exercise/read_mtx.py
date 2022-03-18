

#define read file function
def read_matrix(file):
    fp   = open(file, "r")
    line = fp.readline()
    mtx  = []   
    mm = 0 
    while line :
#    print("line = ", line)
        mtx.append([])
        str_list = line.split()
#    print("str_list = ", str_list)
        for ii in str_list:
            jj = float(ii)
            mtx[mm].append(jj)
#           print(mtx)
#       print("exit for loop")
        mm = mm+1
#       print("mm = ", mm)
        line = fp.readline()
    return mtx

file1 = "./file1.txt"
matrix_1=read_matrix(file1)
print(matrix_1)

file2 = "./file2.txt"
matrix_2=read_matrix(file2)
print(matrix_2)


fname = "./out.txt"
fout = open(fname, "w")

#write_matrix
def write_matrix(matrix_name):
    for ii in matrix_name:
        for jj in ii:
            fout.write("%f "%(jj))
        fout.write("\n")
    return

m1=write_matrix(matrix_1)
m2=write_matrix(matrix_2)



