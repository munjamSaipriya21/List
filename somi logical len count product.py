# a=['a','ab','abc','abcd','abc',"abyk"]

# i=0
# dict={}
# while i<len(a):
#     pres_len=len(a[i])
#     if pres_len not in dict:
#         dict[pres_len]=1
#     else:
#         j=0
#         flag=False
#         while j<i:
#             if a[j]==a[i]:
#                 flag=True
#             j=j+1
#         if not flag:
#             dict[pres_len]=dict[pres_len]+1
#     i+=1
# for key in dict:
#     if dict[key]>1:

#        print(pow(key,dict[key]))
def compare(a,b):
    i=0
    while i<len(a):
        if a[i]==b[i]:
            return False
        i+=1
    return True
a=['a','ab','abc','abcd',"xyz"]
i=len(a)-1
while i>=0:
    j=i-1
    if a[i]!=" ":
        len_curr=len(a[i])
        res=len_curr
        while j>=0:
            if a[j]!=" ":
                if len(a[j])==len_curr and compare(a[j],a[i]):
                    res=res*len_curr
                    a[j]=" "
            j-=1
        if res>len(a[i]):
            print(res)
    i=i-1


        

    
        





