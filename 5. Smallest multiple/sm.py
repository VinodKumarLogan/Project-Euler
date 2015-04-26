from fractions import gcd
lcm=1
for i in xrange(2,20):
	lcm = i*lcm/gcd(i,lcm)
print lcm