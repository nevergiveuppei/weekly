
##find the maximum value and the mininum value of a sequence given by users

import sys
sys.argv.pop(0)

list=[]

if sys.argv[0] == '-help':
    print("enter a list of numbers one by one: -a add_numbers_split_by_spaces")
    sys.exit(0)

while sys.argv[0] == '-a'and len(sys.argv)>1:
    number=sys.argv[1]
    list.append(number)
    sys.argv.pop(1)
print("list=",list)      


#use for loop to find the maximum value and the minimnm value
maximum=None
for num in list:
    if (maximum is None or num > maximum):
        maximum = num
print('Maximum value:', maximum)

minimum=None
for num in list:
    if (minimum is None or num < minimum):
        minimum = num
print('Minimum value:', minimum)


#use max() and min()
max_v=max(list)
print('Maximum value:', max_v)
min_v=min(list)
print('Minimum value:', min_v)


