fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'dataset1.txt'
# wfile = 'testoutput.txt'

## Open file and create a list of bases
with open(fh, 'r') as f: string = f.readline()
lst = list(string)

## Create a dictionary where key = base and value = count
basecount = dict()
for base in lst : basecount[base] = basecount.get(base, 0) + 1
# for key, value in basecount.items() : print key, value

## Write DNA base counts to the output file
w = open(wfile, 'w')
w.write(str(basecount['A'])+' ')
w.write(str(basecount['C'])+' ')
w.write(str(basecount['G'])+' ')
w.write(str(basecount['T'])+' ')

w.close()
print 'written to file', wfile
