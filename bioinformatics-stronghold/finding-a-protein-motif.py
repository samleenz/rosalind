#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:59:55 2017

@author: slee

Rosalind problem
Findign a protein motif - mprt
 shorthand as follows:
   [XY] means "either X or Y" and {X} means "any amino acid except X.
n gly motif is  N{P}[ST]{P}
"""
#%cd '/Users/slee/programming/rosalind/bioinformatics-stronghold'
import urllib.request
import re
#test_weblink = 'http://www.uniprot.org/uniprot/B5ZC00.fasta'
out = 'outputs/finding-a-protein-motif.txt'
fh = 'datasets/rosalind_mprt.txt'
#fh = 'datasets/test_dataset.txt'
re_express = '(?=(N[^P][ST][^P]))' # expression for n-glycosylation motif
# expression has ?= to allow overlaps
### Import protein names
with open(fh, 'r') as f:
    raw = [line.strip() for line in f]

## create weblinks
weblinks = ['http://www.uniprot.org/uniprot/{}.fasta'.format(x) for x in raw]

### access weblinks - make a dict -)
#test = 'B5ZC00'
fasta_dict = dict()
for i, n in enumerate(weblinks):
    n_fasta =  str(urllib.request.urlopen(n).read()).split('\\n')
    seq = ''.join(n_fasta[1:])
    fasta_dict[raw[i]] = fasta_dict.get(raw[i], seq)

### do pattern matching and create dict with match indices
index_dict = dict()
for i in raw:
    index_pos = [m.start(0) for m in re.finditer(re_express, fasta_dict[i])]
    print(index_pos)
    if len(index_pos) == 0:
#        raw.remove(i)
        continue
    index_dict[i] = index_dict.get(i, index_pos)

id_list = []
for i in raw:
    if not i in index_dict.keys():continue
    id_list.append(i)

### save output file - issues with order of output for answer?
#with open(out, 'w') as w:
#    for i in index_dict.keys():
##        if len(index_dict[i]) == 0: continue
#        ind = ''
#        for n in index_dict[i]:
#            ind += str(n) + ' '
#        w.write(str(i+'\n'))
#        w.write(ind)
#        w.write('\n')
#        
with open(out, 'w') as w:
    for i in id_list:
        ind= ''
        for n in [x+1 for x in index_dict[i]]: # add one to correct for 0 based numbering
            ind += str(n) + ' '
        w.write(str(i+'\n'))
        w.write(ind)
        w.write('\n')        
#==============================================================================
# test lines below
#==============================================================================

#urllib.request.urlopen(weblink).read()
#
#
#
#
#index_pos= [(m.start(0), m.end(0)) for m in re.finditer(re_express, fasta_dict[test])]