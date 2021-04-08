# Name-->CHANDER SHEKHAR
 #  Roll-->1/17/FET/BCS/056 (8CSA)

from random import randrange
randomNums=[0]*10	
randomNums[0] = 5 


	
for i in range(1, 10): 
		
	randomNums[i] = ((randomNums[i - 1] * 3) +
										3) % 7 
print("Random Number using congurent")
for i in randomNums: 
	print(i, end = " ") 
print("\nRandom number using built-in functions")
for i in range(10):
    print(randrange(10),end=" ")
