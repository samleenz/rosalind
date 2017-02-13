from itertools import permutations
from operator import add
from functools import reduce
# wfile = raw_input('write to filename:')

wfile = 'enumerating-gene-orders-output.txt'
# n = 3 # NOTE: Sample n value
# NOTE: Activate try/except once program ready to use
try: n = int(input('Please enter the value for n:'))
except:
    print ('This is not a number')
    exit

# NOTE: cerate list of integers {1,...,n}
intlst = [i+1 for i in range(n)]

# NOTE: use itertools.permutations to create a list of the permutations
lst = [i for i in permutations(intlst,)]
# print (lst)

# NOTE: create a list with the permuations in the desired format
lsta=[]
for i in range(len(lst)):
    perm = ''
    for y in range(len(lst[i])): perm += str(lst[i][y])+' '
    lsta.append(perm)
# print (len(lst))
# for item in lsta: print (item)

# NOTE: Write answer to file
w = open(wfile, 'w')
w.write(str(len(lst))+ '\n')
for lines in lsta:
    w.write(str(lines)+'\n')
w.close()
print ('written to file', wfile)
