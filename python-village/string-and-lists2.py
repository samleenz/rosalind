import re
## Open file, set up string
fh = raw_input('filename:')
try : fhandle = open(fh)
except : exit()
fline = fhandle.readline().rstrip() ##read string of interest
## Parse file to find variables a, b, c, and d
for line in fhandle : x = re.findall('^[0-9\s]+' , line)
nums = x[0]
x = nums.split()
# print 'test:', fline
# print len(x)
## assign slice positions
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
# print a, b, c, d ##Test
## Locate slices of interest
section1 = fline[a:b+1]
section2 = fline[c:d+1]
# ## Return result
print section1, section2
