import re
# fh = raw_input('data import filename:')
# wfile = raw_input('write to filename:')
fh = 'dataset5.txt'
wfile = 'testoutput.txt'

## Open file and create a DNAseq string and motif string
with open(fh, 'r') as f:
    DNAseq = f.readline()
    motif = f.readline()
DNAseq = list(DNAseq.rstrip())
motif = list(motif)
# print 'DNA:',DNAseq, '\n', 'Motif:', motif ## check strings correct

## use regular expression to find location of motif in DNAseq
# x = re.findall(motif, DNAseq)
# for i in x:
#     print DNAseq.index(i)
poslst = []
pos = 0
# print 'm:', motif[pos], 'D:', DNAseq[pos]
for base in DNAseq:
    for i in motif:
        if pos == len(motif):
            print 'pos = motif length'
            break
        if not motif[pos] == DNAseq[pos]:
            pos +=1
            print 'not equal'
            continue
        print "i:", i, 'n:', base
        print 'm base:', motif[pos], 'D base:', DNAseq[pos]
        pos +=1
        if pos > len(motif):
            print 'I am here'
            poslst.append(base.index())
            pos=0
    print 'loop'
print poslst



# ## Write motif positions to the output file
# w = open(wfile, 'w')
# for pos in motiflst: w.write('pos')
# w.close()
# print 'written to file', wfile
