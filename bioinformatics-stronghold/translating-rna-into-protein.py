fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'testdataset.txt'
# wfile = 'testoutput.txt'
cfh = 'codon-table.txt'


## Open file and create a list of bases
with open(fh, 'r') as f: RNAseq = f.readline()
mRNAlst = list(RNAseq)
# NOTE: Create a dict that is the codon table Key = codon, Value = aa
codontable = dict()
with open(cfh, 'r') as c:
    for line in c:
        line = line.rstrip()
        (a, b) = line.split()
        # print 'codon:', a, 'amino-acid:', b # NOTE: check tuples
        codontable[a] = codontable.get(a, b)
# print codontable # NOTE: check the codon table

# NOTE: Create a list of codons from mRNA
seqlen = len(mRNAlst)
n = 0 # iterable that will set pos 1 of codons
codonlst = []
for i in range(seqlen):
    if not (i) < (seqlen/3): break # Stop the loop once the last codon is reached
    codonlst.append(mRNAlst[n:(n+3)])
    try: codonlst[i] = ''.join(codonlst[i])
    except: pass
    # print codonlst # NOTE: check that list is correct
    n = n + 3
# for a in range(len(codonlst)): print (a+1), codonlst[a]

# NOTE: Convert the codons to aa's
aalst = []
for i in range(len(codonlst)):
    for codon in codontable:
        # print codontable[codon]
        if codonlst[i] == codon:
            if codon == 'Stop':break
            aalst.append(codontable[codon])
if 'Stop' in aalst: del aalst[aalst.index('Stop')]
protseq = ''.join(aalst)
print 'AA string is :', protseq

# Write protein string to file
w = open(wfile, 'w')
w.write(protseq)
w.close()
print 'written to file', wfile
