h13=int(input())
temp=h13
val1=0
while(h13>0):
     n=h13%10
     val1=val1*10+n
     h13=h13//10
if(temp==val1):
     print("yes")
else:
     print("no")
