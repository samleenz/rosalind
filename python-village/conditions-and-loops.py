##Fetch and store +ve integers
fh = raw_input('filename:')
# fh = 'sampletext2.txt'
with open(fh, 'r') as f: fline = f.readline().rstrip()
spacepos = fline.find(' ')
a = int(fline[:spacepos])
b = int(fline[spacepos+1:])
print a, b ## a, b test
## See if a is even or odd // if even add 1
remainder = a % 2
if a % 2 == 0 : num = a + 1
else: num = a
## Find the sum of odd numbers from a through b
total = 0
while True:
    total = total + num
    num = num + 2
    # print total
    if num > b : break
print 'final total:', total
