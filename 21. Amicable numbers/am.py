def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
numbers=dict()
for i in xrange(1,10000):
	numbers[i] = sum(factors(i)) - i
amicable=0
for i in xrange(1,10000):
	if i != numbers[i] and numbers[i] in numbers:
		if i == numbers[numbers[i]]:
			print i
			amicable+=i
print amicable