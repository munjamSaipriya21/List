list1=[1,2,3,4,5,6,8]
i=0
b=[]
n=int(input("enter the number:"))
while i<len(list1):
  j=1
  c=[]
  while j<=n:
    d=j+i
    # print(d)
    c.append (d)
    j+=1
  i+=n
  b.append(c)
print(b)