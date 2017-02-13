# fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
fh = 'rosalind_hamm.txt'
# wfile = 'testoutput.txt'

f = open(fh, 'r')
c = 0
lst = []
for line in f:
    lst.append(list(line.rstrip()))
lsts = lst[0]
lstt = lst[1]
hd=0
for i in range(len(lsts)):
    if lsts[i] == lstt[i]: continue
    else: hd = hd + 1
print hd


# Write answer to file
w = open(wfile, 'w')
w.write(str(hd))
w.close()
print 'written to file', wfile


# NOTE: Need to make this handle multi line sequence inputs
