fh = raw_input('data import filename:')
wfile = raw_input('write to filename:')
# fh = 'testdataset.txt'
# wfile = 'testoutput.txt'

## Open file and assign variables
with open(fh, 'r') as f: string = f.readline()
lst = string.split()
(k, m, n) = lst
k = int(k)
m = int(m)
n = int(n)
# print k, m, n ## Check variable values
prob = [] ## A list to store P(A)
## Set up initial probabilities
popn = float(k + m + n) ##population size
pA = (k + m)/ popn ## P(indivdual with A allele)
pa = (m + n)/ popn ## P(individual with a allele)
pAA = k / popn
pAa = m / popn
paa = n / popn
## create dictionary with initial probabilities
probdict = {'AA': pAA, 'Aa' : pAa, 'aa' : paa}

## Probability calculations for parent one
##If x is AA - This is good - add to prob
prob.append(pAA)
##If x is Aa then A - this is good - add to prob
prob.append(pAa*0.5)
## If x is Aa then a, return to var probAa_a for round two
prob_Aa_a = pAa*0.5
## If x is aa, return to var prob_aa for round two
prob_aa  = paa

###Probability claculations for parent two
popn += -1
pAA2 = k / popn ## p(AA) for parent 2
## if person one was Aa
pAa2 = (m-1) / popn ## for followup to prob_Aa_a
##followup to prob_Aa_a - if parent 2 is AA
prob.append(prob_Aa_a*pAA2)
##followup to prob_Aa_a - if parent2 is Aa
prob.append(prob_Aa_a*(pAa2*0.5))
## if person one was aa
pAa2 = m / popn ## for followup to prob_aa
prob.append(prob_aa*pAA2) ## and parent 2 aa
prob.append(prob_aa*(pAa2*0.5))

print sum(prob)
# Write P(p1 contains A) to file
w = open(wfile, 'w')
w.write(str(sum(prob)))
w.close()
print 'written to file', wfile
