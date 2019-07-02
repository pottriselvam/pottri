po=int(input())
if po>1:
  for i in range(2,po):
    if po%i == 0:
      print("no")
      break
  else:
      print("yes")
else:
    print("no")
