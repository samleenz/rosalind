#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sam Lee | 28 June
# Enumerating k-mers Lexicographically

# Given: A collection of at most 10 symbols defining an ordered alphabet,
# and a positive integer n (n≤10).
#
# Return: All strings of length n: that can be formed from the alphabet, ordered
#  lexicographically (use the standard order of symbols in the English alphabet).

# sample data
fh = '/Users/slee/programming/rosalind/bioinformatics-stronghold/datasets/testdataset.txt'
wfile = 'testoutput.txt'

with open(fh, 'r') as f:
    alphabet = f.readline().strip().split()
    length = int(f.readline().strip())

for i in range(0,alphabet):
