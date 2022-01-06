a=['my name is priya']
i=0
a
count=0
while i<len(a):
	j=0
	c=0
	while j<len(a[i]):
		if a!=' ':
			c=c+1
		j+=1
	i+=1
	count+=1
print(c)
# print(count)