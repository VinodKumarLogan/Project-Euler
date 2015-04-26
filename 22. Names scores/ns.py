import sys
c=0
for line in sys.stdin:
	names = line.strip().split(",")
names.sort()
score=0
i=1
for name in names:
	score+=i*sum([ord(c)-64 for c in name[1:-1]])
	i+=1
print score