p=int(input())
sum=0
a=p
while p>0:
	c=p%10
	sum=sum+c*c*c
	p=p//10
if a==sum:
	print("yes")
else:
	print("no")
