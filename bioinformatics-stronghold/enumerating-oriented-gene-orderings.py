#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:43:24 2016
Enumerating gene Orderings: Roaslind
Given: A positive integer n≤6
Return: The total number of signed permutations of length n,followed by a list
of all such permutations (you may list the signed permutations in any order).
Sample Dataset
--------------
2

Sample Output
-------------
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
@author: slee
"""
from itertools import permutations, product
#fh = raw_input('data import filename:')
#wfile = raw_input('write to filename:')
fh = 'datasets/testdataset.txt'
wfile = 'outputs/testoutput.txt'

## Open file and create a list of bases
with open(fh, 'r') as f: n = int(f.readline())

pLst = list(permutations(range(1,n+1)))

sLst = list(product('+-', repeat=n))



## Write RNA sequence to the output file
w = open(wfile, 'w')
w.write('This is not the answer')
w.close()
print('written to file', wfile)

