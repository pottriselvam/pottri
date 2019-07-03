from itertools import combinations
psd,n2d=input().split()
n2d=int(n2d)
l=[]
dd=combinations(psd,len(psd)-n2d)
for i in list(dd):
  l.append("".join(i))
print(min(l))
