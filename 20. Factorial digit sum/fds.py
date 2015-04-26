def factorial(n):
	fact=1
	for i in xrange(1,n+1):
		fact*=i
	return fact

print sum([int(i) for i in str(factorial(100))])