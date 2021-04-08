
performance=sample(6:15, 10, replace=TRUE)
weight=sample(1000:6000, 10, replace=TRUE)
print(cov(performance,weight))
print(cor(performance,weight))
counts <- table(performance, weight)
barplot(counts, main="Performance  VS Weight",
  xlab="Performance in gallons/miles ", col=c("darkblue","red"),
  legend = rownames(counts), beside=TRUE)