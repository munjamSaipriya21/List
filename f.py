s="aab"
i=0
s1=[]
s2=[]
while i<len(s):
    j=0
    # s2=[]
    while j<len(s[i]):
        s2.append(s[i])
        # s2.append(s[j])
        j+=1
    s1.append(s2)
    i+=1
print(s1)



