# Python program to find sum of given 
# series. 

def productPrimeFactors(n): 
	product = 1

	for i in range(2, n+1): 
		if (n % i == 0): 
			if isPrime := next(
				(0 for j in range(2, int(i / 2 + 1)) if (i % j == 0)), 1
			):
				product = product * i 

	return product 
	
	
	
# main() 
n = 44
print (productPrimeFactors(n)) 

# Contributed by _omg 
