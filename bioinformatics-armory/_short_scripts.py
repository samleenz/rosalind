#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 21:43:00 2017

@author: root
"""

from Bio.Seq import Seq

x = input("Please paste seq data")

my_seq = Seq(x)

print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))

from Bio import Entrez
Entrez.email = "samuel.lee@vuw.ac.nz"

with open("/Users/slee/Downloads/rosalind_gbk.txt", 'r') as r:
    vals = [line.strip() for line in r]

query = "{}[Organism]".format(vals[0]) + " {}:{}[Publication Date]".format(vals[1],vals[2])
handle = Entrez.esearch(db ="nucleotide",  term = query)
record = Entrez.read(handle)
record["Count"]


from Bio import SeqIO

with open("/Users/slee/Downloads/rosalind_frmt.txt", 'r') as r:
    ids = [line.strip() for line in r]
    
handle = Entrez.efetch(db="nucleotide", id = id, rettype = "fasta")
records = list (SeqIO.parse(handle, "fasta"))

minseq = 10000000000000000000
for seq in records:
    if len(seq.seq) < minseq:
        minseq = 