#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:46:36 2017

@author: slee
"""
import numpy

fh = '/Users/slee/Desktop/programming/rosalind/bioinformatics-stronghold/datasets/cons_data_test.txt'
dnaList=[]
with open(fh,'r') as f:
    for line in f:
        if not line.startswith('>'):
            dnaList.append(list(line.strip()))

dnaArray = numpy.array([x for x in dnaList])           


profileMatrix = numpy.array(['A:','C:','G:','T:'])
profileMatrix.shape = 4,-1

profileDict = {'A:': [], 'C:': [], 'G:': [], 'T:': []}


x = [i[0] for i in dnaArray]

profileDict = {}
for n in [i[0] for i in dnaArray]:    
    if  n== 'A': profileDict['A'] = profileDict.get('A',0) + 1
    elif n == 'C': profileDict['C'] = profileDict.get('C',0) + 1
    elif n == 'G': profileDict['G'] = profileDict.get('G',0) + 1
    elif n == 'T': profileDict['T'] = profileDict.get('T',0) + 1

maxKey = ('',0)
for i in profileDict.keys():
    if profileDict[i] > maxKey[1]:
        maxKey = (i,profileDict[i])
    

