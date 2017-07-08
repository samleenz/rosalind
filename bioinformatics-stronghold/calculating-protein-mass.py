# fh = raw_input('data import filename:')
# wfile = raw_input('write to filename:')
fh = '/Users/slee/programming/rosalind/bioinformatics-stronghold/datasets/rosalind_prtm.txt'
wfile = 'outputs/testoutput.txt'
afh = 'datasets/aa-weight.txt'

# NOTE: Create a dict that is the aa weight table Key = aa, Value = weight
weighttable = dict()
with open(afh, 'r') as c:
    for line in c:
        line = line.rstrip()
        (a, b) = line.split()
        # print 'codon:', a, 'amino-acid:', b # NOTE: check tuples
        weighttable[a] = weighttable.get(a, float(b))
print weighttable # NOTE: check the aa weight table

# NOTE: create a string with the aa sequence
with open(fh, 'r') as f: aaseq = f.readline()
# mRNAlst = list(RNAseq)
print aaseq

# NOTE: create a list with the aa weights
wlst = []
for i in range(len(aaseq)): # NOTE: loop length is aa seq length
    for aa in weighttable: # NOTE: compare each aa and assign the correct weight
        if aaseq[i] == aa: wlst.append(weighttable[aa])
weight = str(sum(wlst))
print 'Weight of string:', weight,
# # Write protein string to file
# w = open(wfile, 'w')
# w.write(weight)
# w.close()
# print 'written to file', wfile
