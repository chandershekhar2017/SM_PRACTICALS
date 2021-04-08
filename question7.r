  
 mode <- function(x) {
     ux <- unique(x)
     ux[which.max(tabulate(match(x, ux)))]
 }
 
 list <- c(1,2,3,4,5,1,2,3,1,2,4,5,2,3,1,1,2,3,5,6) 
 list2 <- c(1,2,3,4,5,4,2,3,1,2,4,5,4,3,1,3,2,6,5,6)
 print (mean(list))
 print(median(list))
 print(mode(list))
 print(var(list))
 print(sqrt(var(list)))
 print(cor(list,list2))
