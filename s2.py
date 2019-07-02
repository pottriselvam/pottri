num12=int(input())
num=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,num12):
    num*=10
    num+=int(array[a])
print(num)
