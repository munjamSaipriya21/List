a=[1,2,3,4,5,6]
i=1
n=int(input("entr the number:"))
b=[]
while i<len(a):
    j=0
    c=[]
    while j<n:
        d=i+j
        c.append(d)
        j+=1
    b.append(c)
    i+=1
print(b)

