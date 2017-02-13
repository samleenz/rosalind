################################################
# Write another version that converts to protein first, might take less code?
################################################
# NOTE: Functions used

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

def translated_codons(startcodon, DNAstring):
    '''
    * Function to create a lst of codons for a reading frame that starts
      at an ATG and goes to a stop codon
    * Once a stop codon is reached a list of codons is returned
    * If it reaches the end of the sequcence before a stop, 'None' is returned
    * Parameter 'startcodon' is index for 'A' in start codon
    * Parameter 'DNAstring' is the sequence to be parsed
    * Create the empty stringlst list before calling function!
    '''
    codonlst = []
    n = startcodon # NOTE: iterable for codon position
    for i in range(len(DNAstring[x:])):
        if n+3 > len(DNAstring):
            return None
            # NOTE: will return none if the end of the seq is reached before a stop codon
            # return codonlst
        # print('DEBUG:', DNAstring[n:n+3])
        if codontable[(DNAstring[n:n+3])] =='_' :
            print('Stop codon:', DNAstring[n:n+3])
            # stringlst.append(codonlst)
            # return stringlst
            return codonlst
        codonlst.append(DNAstring[n:(n+3)])
        try: codonlst[i] = ''.join(codonlst[i])
        except: pass
        n+=3


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
    for (old, new) in zip(fwd, rev):
        rDNAstring = rDNAstring.replace(old, new)
    return rDNAstring


################################################
# NOTE: Start program from here

fh = input('data import filename:')
wfile = input('write to filename:')
# fh = 'testdataset.txt'
# wfile = 'testoutput.txt'
import re

# NOTE: Import the DNA sequence and create the codon table
seqdict = parse_fasta(fh)
for k, v in seqdict.items(): DNAstring = v
codontable = DNA_codon_table()
# NOTE: Create the reverse complement and make a list with the two sequences
rDNAstring = reverse_complement(DNAstring)
seqlst = [DNAstring, rDNAstring]

stringlst = [] # NOTE: List to hold the list of codons for each ORF
peptidelst =[] # NOTE:  List for final aa sequences
# NOTE: For loop to run the main functions for both sequences
for seq in seqlst:
    # NOTE: First this finds all the start codons
    startpos =[] # NOTE: List for ATG index positions (of A)
    x = re.compile('ATG')
    for m in x.finditer(seq):
        startpos.append(m.start())
    # x = DNAstring.find('ATG')
    print('Locations of ATG:',startpos)

    # NOTE: Section to create list of codons from each start codon only if
    # NOTE: there is a stop codon to close the ORF
    for x in startpos:
        # print (type(x))
        codons  = translated_codons(x, seq)
        if codons != None: stringlst.append(codons)
        # print ('current strings:', stringlst)

    # NOTE: Section to translate each list of codons in the list stringlst
    for n in range(len(stringlst)):
        codonlst = stringlst[n]
        peptide =''
        for i in range(0, len(codonlst)):
                codon = codonlst[i]
                amino_acid = codontable.get(codon, '*')
                if amino_acid == '_':
                    break
                peptide += amino_acid
        # NOTE: Once translated, peptide only saved if not already present
        if not peptide in peptidelst:
            peptidelst.append(peptide)


print('These are the ORFs I found')
for i in stringlst: print(i)
print ('This is my answer')
for i in peptidelst: print(i)

# # NOTE: Sample dataset answer
# print('The Correct answer is: \n',
# 'MLLGSFRLIPKETLIQVAGSSPCNLS \n',
# 'M \n',
# 'MGMTPRLGLESLLE \n',
# 'MTPRLGLESLLE')


# NOTE: Write protein string to file
w = open(wfile, 'w')
for i in range(len(peptidelst)):
    w.write(str(peptidelst[i] + '\n'))
w.close()
print ('written to file', wfile)
