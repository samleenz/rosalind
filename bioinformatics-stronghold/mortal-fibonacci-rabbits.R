# Given: Positive integers n≤100 and m≤20
# 
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# test n 6 m 3
# out = 4

y <- readLines(con = 'datasets/rosalind_fibd.txt')
y <-  as.numeric(unlist(strsplit(y, split = " ")))

fibovalsM <- numeric(y[1])
fibovalsM[1] <- 1
fibovalsM[2] <- 1
# fibovalsM[3] <- fibovalsM[2] + fibovalsM[1]
for (i in 3:y[1]) {
  fibovalsM[i] <- fibovalsM[i-1] + fibovalsM[i-2] - (fibovalsM[i-1] - fibovalsM[i-2])
}
# out <- sum(fibovalsM[1:y[2]])
# paste(out)
plot(1:y[1], log(fibovalsM))
(fibovalsM[1:6])
