def factorial(n):
	fact=1
	for i in xrange(1,n+1):
		fact*=i
	return fact

print factorial(40)/(factorial(20)**2)