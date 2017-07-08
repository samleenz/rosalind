# 07 June
# Sam Lee
# Consensus and Profile
# 
# 
# Given: A collection of at most 10 DNA strings of equal length
# (at most 1 kbp) in FASTA format.
# 
# Return: A consensus string and profile matrix for the collection.
# (If several possible consensus strings exist, 
# then you may return any one of them.)

# implemented using seqinr
# redo wth base R at some point


# packages / parameters ---------------------------------------------------

library(seqinr)

dir <- "/Users/slee/programming/rosalind/bioinformatics-stronghold"

fname <- "rosalind_cons.txt"

# read in the file --------------------------------------------------------

raw <- read.alignment(file = file.path(dir, "datasets", fname),
                      format = "fasta",
                      forceToLower = F)




# create consensus matrix -------------------------------------------------

cons <- consensus(raw, method = "majority")

prof <- consensus(raw, method = "profile")


# write output ------------------------------------------------------------

writeLines(c(cons, "\n"),
           con = file.path(dir, "outputs", "consensus-and-profile-r.txt"),
           sep = "")

write.table(prof, file = file.path(dir, "outputs", "consensus-and-profile-r.txt"),
      append = T,
      col.names = F,
      row.names = c("A:", "C:", "G:", "T:"),
      quote = F)
