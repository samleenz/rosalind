fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'dataset4.txt'
# wfile = 'testoutput.txt'

## Open file and create a list of bases
with open(fh, 'r') as f: DNAseq = f.readline()
lst = list(DNAseq)
rlst = []
## Create list of complement sequence
for base in lst:
    # print base
    if base == 'A': rlst.append('T')
    if base == 'T': rlst.append('A')
    if base == 'C': rlst.append('G')
    if base == 'G': rlst.append('C')
## create the reverse complmenet sequence
rclst = []
i = 0
findex = len(rlst) - 1
for base in rlst:
    rclst.append(rlst[findex - i])
    i = i + 1
rDNAseq = ''.join(rclst)

# print rDNAseq
# Write reverse complement sequence to the output file
w = open(wfile, 'w')
w.write(rDNAseq)
w.close()
print 'written to file', wfile
