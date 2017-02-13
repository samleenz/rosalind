fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'dataset2.txt'
# wfile = 'testoutput.txt'

## Open file and create a list of bases
with open(fh, 'r') as f: DNAseq = f.readline()
lst = list(DNAseq)

## Parse lst and Replace 'T' with 'U' to create RNAseq
for base in lst :
    try :
        tpos = lst.index('T')
        lst[tpos] = 'U'
    except: break
RNAseq = ''.join(lst)

## Write RNA sequence to the output file
w = open(wfile, 'w')
w.write(RNAseq)
w.close()
print 'written to file', wfile
