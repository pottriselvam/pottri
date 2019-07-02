it=int(input())
le=[int(x) for x in input().split()[:it]]
for u in le:
  if(le.count(u)==1):
    print(u,end=" ")
