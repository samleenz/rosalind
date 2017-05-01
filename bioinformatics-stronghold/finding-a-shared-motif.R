
# 1 Read file in to a table
x <- readLines(con = 'datasets/test_dataset.txt')
dna_seqs <- (x[seq(from = 2, to = length(x), by = 2)])

#2 create nested list with each sequences substring




#3 sort each of the substring lists in place




#4 iterate through first nested list to find the LCS