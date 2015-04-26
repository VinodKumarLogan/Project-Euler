import sys
pmax=0
for i in xrange(999,101,-1):
	for j in xrange(999,101,-1):
		if i%10!=0 and j%10!=0:
			prod=str(i*j)
			if prod == prod[::-1]:
				if int(pmax)<int(prod):
					pmax=prod
print pmax