fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'sampletext4.txt'
lines = []
with open(fh, 'r') as f:
    for line in f : lines.append(line.rstrip())
# for i in lines: print i ## test that list created correctly
n = len(lines)/2
x = 0
for i in range(n):
    del lines[x]
    x = x + 1


# print 'length:', len(lines)
# for i in lines: print i

# wfile = 'output1.txt'
w = open(wfile, 'w')
for line in lines: w.write(str(line) + '\n')
w.close()
print 'written to file', wfile
