def check(q,l):
    x=l[0]
    p = []
    for i in range(len(q)):
        for j in range(1,len(l)):
            y=l[j]
            if j==(len(l)-1) and x[i] == y[i]:
                p.append(x[i])
            elif x[i] == y[i]:
                continue
            else:
                return p
    return p
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
q=min(l)
print("".join(check(q,l)))
