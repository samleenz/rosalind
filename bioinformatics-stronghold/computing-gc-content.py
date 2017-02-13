import re

def cg_calc(string):
    ## Where string is the DNA sequence
    basecount = {}
    lst = list(string)
    ##create dict where key = base and value = count - also with a total base count
    for base in lst :
        basecount[base] = basecount.get(base, 0) + 1
        basecount['total'] = basecount.get('total', 0) + 1
    # for key, value in basecount.items() : print key, value
    ## calculate CG content
    CGcontent = (int(basecount['C']) + int(basecount['G'])) / float(basecount['total'])
    seqdict[ID] = CGcontent*100 ## replace DNAseq in seqdict with CG percent
    # print 'CG-content', ID, ':', CGcontent*100 ## To view results of the CG calc ## function to calculate CG content of a dict of ID/seq pairs ## Function to calculate the CG content of a string


# fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
fh = 'rosalind_gc.txt'
# wfile = 'testoutput.txt'

# NOTE: Create a dict of ID/seq pairs from a FASTA file
re_ID = '^>(.+_[0-9]+)' ##regular expression to take ID
seqdict = {}
lst = []
## Open file and create a dict of ID/seq pairs and a list of IDs
f = open(fh, 'r')
c = 0
for line in f:
    line = line.rstrip()
    x = re.findall(re_ID, line)
    if len(x) > 0: ## If line an ID, create a new entry in dict
        x = ''.join(x) ## convert ID from list to string
        seqdict[x] = seqdict.get(x, '')
        lst.append(x)
        index = lst.index(x)
        # print x, index ## Prints the current ID, and it's index
    if not len(x) > 0: ## If not an ID line, append line to value of latest ID key
        # print lst[index] ,line[:4]
        seqdict[lst[index]] = seqdict.get(lst[index], '') + line
f.close()

### Do the CG-content calculation and update seqdict
for ID in seqdict: cg_calc(seqdict[ID])

## Find the max CG-content with respect to ID
CGcontentlst = []
for k, v in seqdict.items():
    CGcontentlst.append(v) ## create a list of CG-content
    if seqdict[k] == max(CGcontentlst) : (ID, CG) = (k, seqdict[k])
# print ID, CG
# ## Write highest CG content line + ID to the output file
w = open(wfile, 'w')
w.write(str(ID))
w.write('\n')
w.write(str(CG))
w.close()
print 'written to file', wfile
