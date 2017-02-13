## Function to create a dict of ID/seq pairs from a FASTA file

import re
fh = 'rosalind_gc.txt'

##regular expression to take ID
re_ID = '^>(.+_[0-9]+)'
## Open file and create a list of lines
seqdict = {}
lst = []
f = open(fh, 'r')
c = 0
for line in f:
    line = line.rstrip()
    x = re.findall(re_ID, line)
    if len(x) > 0: ## If line an ID, create a new entry in dict
        x = ''.join(x) ## convert from list to string
        seqdict[x] = seqdict.get(x, '')
        lst.append(x)
        index = lst.index(x)
        # print x, index
    if not len(x) > 0: ## If not an ID line, append line to value of latest ID key
        # print lst[index] ,line[:4]
        seqdict[lst[index]] = seqdict.get(lst[index], '') + line

# for k, v in seqdict.items(): print 'ID:', k, 'seq:', v
