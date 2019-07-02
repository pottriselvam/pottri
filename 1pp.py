l = int(input())
P = list(map(int,input().split()))
r = []
for i in range(len(P)):
    if P.count(P[i]) > 1:
        if P[i] not in r:
            r.append(P[i])
r.sort()
if len(r)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
 
