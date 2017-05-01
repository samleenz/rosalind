#==============================================================================
# Recursion was a bad idea -- there are a lot of possible options...
# maybe try implement in R?
#==============================================================================




%cd '/Users/slee/programming/rosalind/bioinformatics-stronghold'
import re
import itertools
import sys
#==============================================================================
# functions
#==============================================================================
def parse_fasta(filename):
    '''
    * Create a dictionary of ID/seq pairs from a FASTA file
    * Return the dictionary as seqdict
    * arguemnt is the variable that has had the filename to be parsed
      assigned to it
    '''
    import re
    re_ID = '^>(.+_[0-9]+)' ##regular expression to take ID
    seqdict = {}
    lst = []
    ## Open file and create a dict of ID/seq pairs and a list of IDs
    f = open(filename, 'r')
    for line in f:
        line = line.rstrip()
        x = re.findall(re_ID, line)
        if len(x) > 0: ## If line an ID, create a new entry in dict
            x = ''.join(x) ## convert ID from list to string
            seqdict[x] = seqdict.get(x, '')
            lst.append(x)
            index = lst.index(x)
            # print x, index ## Prints the current ID, and it's index
        if not len(x) > 0: ## If not an ID line, append line to value of latest ID key
            # print lst[index] ,line[:4]
            seqdict[lst[index]] = seqdict.get(lst[index], '') + line
    f.close()
    return seqdict



def sub_wrap(seq):
    '''
    wrapper for substr to correct scope of list used for string storage
    '''
    lst = []
    def substr(seq):
     '''
     return all substrings of a string that begin from the beginning of the string     
     '''
     if len(seq) == 0: 
#         print("length is 0 and list contains{} and seq is {}".format(lst,seq))
         return lst        
     else: 
#         print("list contains{} and seq is {}".format(lst,seq))
         lst.append(seq)
         return substr(seq[:-1])
#    print(lst)
    return substr(seq)




def sub_wrap_wrap(fullseq):
    '''
     wrapper function to apply substr from each base from left to right in string
     returns a set of the substrings found
    '''
    comb_substr=[]
    for i in range(len(fullseq)):
        comb_substr.append(sub_wrap(fullseq[i:]))
#        print(sub_wrap(fullseq[i:]))
    substrings = list(itertools.chain.from_iterable(comb_substr))
    return set(substrings)

def string_sort(string_list):
    '''
    requires the parameter to be a list, not a set
    sorts strings by length
    takes a list of strings
    '''
    tup_lst = []
    for i, n in enumerate(string_list):
        tup_lst.append((len(n),i))
    tup_lst = sorted(tup_lst, reverse=True)
    return [string_list[i[1]] for i in tup_lst]




#==============================================================================
#  script - for recursive approach
#==============================================================================

#1 locate and import file in / file out
#fh = 'datasets/test_dataset.txt'
#wfile = 'outputs/testoutput.txt'
 fh = 'datasets/rosalind_lcsm.txt'
 wfile = 'finding-a-shared-motif-output.txt'
seqdict = parse_fasta(fh)
DNAstrings = list(seqdict.values())
#print (DNAstrings)

#2 create nested list with each sequences substring
substr_lst = []
for seqx in DNAstrings:
    substr_lst.append(sub_wrap_wrap(seqx))

#3 sort each of the substring lists in place
for i, n in enumerate(substr_lst):
    substr_lst[i] = string_sort(list(n))

#4 iterate through first nested list to find the LCS

for seq in substr_lst[0]:
    count = 0
    for i in range(len(substr_lst[1:])):
        i +=1 # to correct for skipping 1st list
        if not seq in substr_lst[i]:
            break
        else:
            count +=1 
    if count == len(substr_lst[1:]):
        lcs = seq
        break
#print(lcs) 
 
      
#5 Write answer to file
w = open(wfile, 'w')
w.write(str(lcs))
w.close()
print ('written to file', wfile)
print ('Shared motif was {}'.format(lcs))

#==============================================================================
# script - non recursive approach
#==============================================================================
#1 locate and import file in / file out
#fh = 'datasets/test_dataset.txt'
#wfile = 'outputs/testoutput.txt'
 fh = 'datasets/rosalind_lcsm.txt'
 wfile = 'finding-a-shared-motif-output.txt'
seqdict = parse_fasta(fh)
DNAstrings = list(seqdict.values())

#2 create nested list with each sequences substring
for i in 

#3 sort each of the substring lists in place

#4 iterate through first nested list to find the LCS


#5 Write answer to file
w = open(wfile, 'w')
w.write(str(lcs))
w.close()
print ('written to file', wfile)
print ('Shared motif was {}'.format(lcs))

#==============================================================================
#  test calls
#==============================================================================
testval = 'TAGACCA'

print(sub_wrap_wrap(testval))