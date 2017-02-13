# NOTE: Second verion of program,
# NOTE: translate readings frames to proteins then parse_fasta


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

def DNA_codon_table():
    '''
    * creates a dictionary for the DNA-codon table
    * remember to assign it to a variable, e.g. codondict = DNA_codon_table()
    * consider expanding function to include translation from a start codon
    '''
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    return codontable

def reverse_complement(DNAstring):
    '''
    * Returns the reverse complement of a DNA string
    * Parameter DNAstring is the DNA seq to be reversed
    '''
    rDNAstring = DNAstring[::-1]
    rDNAstring = rDNAstring.lower()
    # NOTE: lowercase to prevent the for loop resulting in only 2 bases
    fwd = ('a','t','c','g')
    rev = ('T','A','G','C')
    # bases = ['A','C','G','T']
    print ('reversed', rDNAstring)
    for (old, new) in zip(fwd, rev):
        rDNAstring = rDNAstring.replace(old, new)
        print (old, new)
        print ('so far:', rDNAstring)
    return rDNAstring


    #################################
    # NOTE: Body of program from here
fh = 'testdataset.txt'
wfile = 'testoutput.txt'
import re

seqdict = parse_fasta(fh)
for k,v in seqdict.items(): DNAstring = v
codontable = DNA_codon_table()
# NOTE: Create the reverse complement and make a list with the two sequences
rDNAstring = reverse_complement(DNAstring)
seqlst = [DNAstring, rDNAstring]

print (seqlst)
