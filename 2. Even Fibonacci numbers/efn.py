fibSum=0
a=0
b=1
n=4000000
while b<n:
	a,b = b,a+b
	if not b&1:
		fibSum+=b
print fibSum,b,a