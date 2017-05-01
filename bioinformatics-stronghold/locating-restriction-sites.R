# 1 / 05 / 17
# Locating Restriction Sites - Rosalind
# Sam Lee
# Given: A DNA string of length at most 1 kbp in FASTA format.
# 
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

# ---- Packages

source("https://bioconductor.org/biocLite.R")
biocLite("Biostrings")

# ---- Code

#1 Read fastq file in
raw_in <- readLines(con = "datasets/test_dataset.txt")
string <- paste(raw_in[-1], sep = "", collapse = "")
string <- strsplit(string, split = "")[[1]]

#2 Create reverse complement sequence object
# rev_string <- rev(string)
rev_string <- string
  # create reverse complement into lower case to avoid duplicaton
rev_string[rev_string == "A"] <- "t"
rev_string[rev_string == "T"] <- "a"
rev_string[rev_string == "G"] <- "c"
rev_string[rev_string == "C"] <- "g"
rev_string <- toupper(rev_string)
#3 Compare for equivalency into sequence id

string_match <- string == rev_string

string
rev_string
## REversing the complement is proving hard to line up with vector methods
# Can visalise it by hard to do computationally

for (n in range(length(string[1]))){
  print(n)
}

#4 Extract all equivalencies with length 4 to 12


#5 Construct the output format and save 


# ----- Test set

# in 

# >Rosalind_24
# TCAATGCATGCGGGTCTATATGCAT

# out

# 4 6
# 5 4
# 6 6
# 7 4
# 17 4
# 18 4
# 20 6
# 21 4