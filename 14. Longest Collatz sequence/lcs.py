longestChain=0
longNum=1
for i in xrange(2,1000000):
	chain=0
	n=int(i)
	while n!=1:
		if n&1:
			n=(3*n)+1
		else:
			n=n>>1
		chain+=1
	if chain>longestChain:
		longestChain=chain
		longNum=i

print longNum, longestChain