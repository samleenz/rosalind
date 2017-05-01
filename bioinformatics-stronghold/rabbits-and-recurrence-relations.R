# created 25/4/17
# Given: Positive integers n≤40 and k≤5
# 
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation,
#         every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# sample n=5 k=3
# out = 19

# A-------
x <- readLines(con = 'datasets/rosalind_fib.txt')
x <-  as.numeric(unlist(strsplit(x, split = " ")))
# x[1] is n motnhs and x[2] isk litter *pairs*
fibovals <- numeric(x[1])
fibovals[1] <- 1
fibovals[2] <- 1
for (i in 3:x[1]) {
  fibovals[i] <- fibovals[i-1] + (fibovals[i-2] * x[2])
}
paste(fibovals[x[1]])
# -----------



len <- 10
fibvals <- numeric(len)
fibvals[1] <- 1
fibvals[2] <- 1
for (i in 3:len) { 
  fibvals[i] <- fibvals[i-1]+fibvals[i-2]
}
sum(fibvals)
