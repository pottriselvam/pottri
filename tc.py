l=[str(i) for i in input().split()]
s1=l[0]
s2=l[1]
p=0
for i in range(0,len(s1)):
    if(s1[i]!=s2[i]):
        p=p+1
if(p>=2):
    print("no")
if(p==1):
    print("yes")
