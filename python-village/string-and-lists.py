fh = raw_input('filename:')
fhandle = open(fh)
# print 'debug:', fhandle
a = int(raw_input('a:'))
b = int(raw_input('b:'))
c = int(raw_input('c:'))
d = int(raw_input('d:'))
for line in fhandle :
    section1 = line[a:b+1]
    # print 'debug:', section1
    section2 = line[c:d+1]
    # print 'debug:', section2
print section1, section2
