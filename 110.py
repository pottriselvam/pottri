
a,s=map(int,input().split())
for v in range(a,s):
   if v>1:
      for i in range(2,v):
        if(v%i)==0:
          break
      else:
          print(v,end=" ")
