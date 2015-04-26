def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

i=4
while True:
	n=i*(i-1)>>1
	f=len(factors(n))
	print i,n,f
	if f>500:
		print i,n
		break
	i+=1