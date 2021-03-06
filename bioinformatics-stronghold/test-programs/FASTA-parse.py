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

fh= 'dataset3.txt'
seqdict = parse_fasta(fh)

print (seqdict)
