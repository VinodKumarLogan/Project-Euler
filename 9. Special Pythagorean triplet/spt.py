from math import sqrt
import sys
for a in xrange(1,1000):
	for b in xrange(a+1,1000):
		c=sqrt((a*a)+(b*b))
		if c.is_integer():
			if (a+b+c)==1000:
				print a*b*int(c)
				sys.exit()