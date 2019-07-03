num,num1=input().split()
PG=abs(len(num)-len(num1))
for i in range(len(num)):
  if len(num1)==1 and num1[i] in num:
   break
  if num[i]!=num1[i]:
   PG+=1
print(PG)
