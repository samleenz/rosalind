fh = raw_input('filename:')
# fh = 'sampletext3.txt'
with open(fh, 'r') as f: fline = f.readline().rstrip()
countdict = dict()
fline = fline.split()
for word in fline :
    countdict[word] = countdict.get(word,0) + 1

for k, v in countdict.items() :
    print k, v
