a="my name is priya"
i=0
s=0
while i<len(a):
    word=""
    while i<len(a) and a[i]!=" ":
        word+=a[i]
        i+=1
    s+=1
    print(s,"space")
    print(s,word)
    i+=1



