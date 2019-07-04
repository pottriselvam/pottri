a,b=input().split(' ')
if(len(a)!=len(b)):
  print('no')
for i in a:
  c=a.count(i)
for i in b:
  p=b.count(i)
if(c==p):
  print("yes")
else:
  print("no")
