num=list(map(str,input()))
ps=ee=0
for i in range(0,len(num)-1):
  q=num[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+num[j]
    if int(q)<27 and int(q)>0: ps=ps+1
    elif int(q)==0: ps=ps-1
    else: break
if ps!=1: ee=ps%2
print(ps+ee+1)
