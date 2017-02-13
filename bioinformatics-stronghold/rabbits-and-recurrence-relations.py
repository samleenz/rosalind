# fh = input('data import filename:')
# wfile = input('write to filename:')
#wfile = 'testoutput.txt'
#fh = 'testdataset.txt'
#with open(fh, 'r') as f: string = f.readline()
#lst = string.split()
#(n, k) = lst
#n = int(n)
#k = int(k)
n=4
k=1
def rabbit(n,k):
    '''
    Where n is number of generations
    and k number of offspring per generatin per pair
    '''
    f0 = 0
    f1 = 1
    for i in range(n):
         fNew = f0 + (f1*k)
         f0 = f1
         f1= fNew
#         print(fNew)   
    return fNew
# NOTE: sample values
n= 5
k= 3

def getFibo():
    yield 1
    yield 1
    formerOfFormer = 1
    former = 1
    while True:
        newVal = formerOfFormer + former
        formerOfFormer = former
        former = newVal
        yield newVal

# NOTE: Write answer to file
# w = open(wfile, 'w')
# w.write('answer')
# w.close()
# print( 'written to file', wfile)
