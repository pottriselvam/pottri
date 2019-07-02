num=int(input())
l=[int(x) for x in input().split()[:num]]
n2=[]
for i in range(0,int(len(l))):
    if(i==l[i]):
        n2.append(i)
if(int(len(n2)))!=0:
    for u in n2:
        print(u,end=" ")
else:
    print(-1)
