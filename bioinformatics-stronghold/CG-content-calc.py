string = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
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
print 'CG-content:', CGcontent*100
