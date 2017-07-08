#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:09:37 2016
Rosaling: Locating Restriction Sites
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.

sample dataset:
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

sampe output:
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

@author: slee
"""
#fh = raw_input('data import filename:')
#wfile = raw_input('write to filename:')
fh = 'testdataset.txt'
wfile = 'testoutput.txt'
fh, wfile = '/dataset'+fh, '/output'+wfile




## Write RNA sequence to the output file
w = open(wfile, 'w')
w.write('This is not the answer')
w.close()
print('written to file', wfile)