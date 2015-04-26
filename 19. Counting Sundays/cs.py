from datetime import datetime,timedelta
count=0
day=datetime.strptime('1901-01-07', '%Y-%m-%d')
end=datetime.strptime('2000-12-31', '%Y-%m-%d')
while day<=end: 
	if day.day==1:
		print day
		count+=1 
	day+=timedelta(days=7)
print count