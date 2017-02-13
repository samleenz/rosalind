import re
def import_fasta(): ##A function to take a fasta file and create a dict of ID/seq pairs and a list of IDs
    re_ID = '^>(.+_[0-9]+)' ##regular expression to take ID
    f = open(fh, 'r')
    c = 0
    for line in f:
        line = line.rstrip()
        x = re.findall(re_ID, line)
        if len(x) > 0: ## If line is an ID, create a new entry in dict
            x = ''.join(x) ## convert ID from list to string
            seqdict[x] = seqdict.get(x, '')
            idlst.append(x)
            index = idlst.index(x)
            # print x, index ## Prints the current ID, and it's index
        if not len(x) > 0: ## If not an ID line, append line to value of latest ID key
            # print lst[index] ,line[:4]
            seqdict[idlst[index]] = seqdict.get(idlst[index], '') + line
    f.close()


###
fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'testdataset.txt'
# wfile = 'testoutput.txt'
cfh = 'codon-table.txt'
answer = 'MVYIADKQHVASREAYGHMFKVCA'
# NOTE: dict and list for import_fasta
seqdict = {}
idlst = []

import_fasta() ##Run function to create the dict with DNA strings+FASTA codes
# for k,v in seqdict.items(): print k, v
# NOTE: rename the key of the actual DNA string to DNAstring
maxvalue = 0
for k,v in seqdict.items():
    # print k, ':', len(v)
    if len(v) > maxvalue:
        # print 'here'
        # print maxkey
        maxvalue = len(v)
        maxkey = k

    # print 'max(k):', maxkey
# maxkey = max(seqdict, key=seqdict.get)
# print 'maxkey', maxkey # NOTE: check that the retreived string is the DNA sequence
seqdict['DNAstring'] = seqdict.pop(maxkey) ## create new entry for the DNA string, remove old one

# NOTE: Search through DNAstring to find introns and remove them
s = seqdict['DNAstring']
print 'DNA sequence:', s
intronlst = []
for key, value in seqdict.items():
    if key == 'DNAstring': continue
    lst = re.findall(value, s)
    print 'lst:', lst
    for item in lst:
        # NOTE: These three prints are to check that the slice for intron is infact the intron
        # print 'position',s.index(item)
        # print 'intron', item
        # print 'sliced intron', s[s.index(item):(s.index(item)+len(item))]
        if item == s[s.index(item):(s.index(item)+len(item))]:#print 'true'
            # print 'before:', s[:s.index(item)]
            # print 'after:', s[s.index(item)+len(item):]
            s = s[:s.index(item)] + s[s.index(item)+len(item):]
            # a = s[:s.index(item)]
            # print 'a:', a
            # b = s[s.index(item)+len(item):]
            # print 'b:', b
            # print 'DNAseq:', s

    intronlst += lst
# print 'intron list:', intronlst
print 'DNA sequence, exons only:', s

# NOTE: Convert the DNA string to mRNA
## Parse lst and Replace 'T' with 'U' to create RNAseq
lst = []
for base in s: lst.append(base)
for base in lst :
    try :
        tpos = lst.index('T')
        lst[tpos] = 'U'
    except: break
RNAseq = ''.join(lst)
print 'RNAseq:', RNAseq


# NOTE: Convert mRNA to codons and then protein sequence
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
seqlen = len(RNAseq)
n = 0 # iterable that will set pos 1 of codons
codonlst = []
for i in range(seqlen):
    if not (i) < (seqlen/3): break # Stop the loop once the last codon is reached
    codonlst.append(RNAseq[n:(n+3)])
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
# # NOTE: Blow used to test sample dataset against answer
# if protseq == answer: print "Correct!"
# else:
#     print 'No, you are wrong. The correct answer is:'
#     print answer

# NOTE: Write protein string to file
w = open(wfile, 'w')
w.write(protseq)
w.close()
print 'written to file', wfile
