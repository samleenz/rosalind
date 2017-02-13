import re
# fh = raw_input('data import filename:')
# wfile = raw_input('write to filename:')
fh = 'rosalind_subs.txt'
wfile = 'inding-a-motif-in-dna-output.txt'

## Open file and create a DNAseq string and motif string
with open(fh, 'r') as f:
    DNAseq = f.readline()
    motif = f.readline()
motif = motif.rstrip()
DNAseq = list(DNAseq.rstrip())
x = len(motif) ## Length of the motif
slicelst = []
# print 'DNAseq:', DNAseq
# print 'motif:', motif
# NOTE: Create a list (slicelst) of DNAseq slices equal to the length of the substring
for i in range(len(DNAseq)):
    if len(DNAseq[i:i+x]) == x :
        y = ''.join(DNAseq[i:i+x])
        slicelst.append(y)
#NOTE: These are checks that lists were created correctly
print 'motif length',len(motif)
print 'slice length',len(slicelst[1])
# print slicelst
# NOTE: search thorugh list of slices for matches to the motif
loclst = [] # list to put the index position of matches into
for i in range(len(slicelst)):
    if motif == slicelst[i]:
        loclst.append(str(i+1))
        # print 'slicelst[i]:', slicelst[i]
print 'motif:', motif, 'length:', len(motif)
# print type(loclst)
output = ' '.join(loclst)
print 'output:', output

# Write result to the output file
# with open(wfile, 'w') as w:
# w = open(wfile, 'w')
# w.write(output)
# w.close()
# print 'written to file', wfile
