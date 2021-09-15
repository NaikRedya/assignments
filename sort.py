a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range (1,len(a)) :
  for j in range(len(a)-i) :
    if a[i][1]>a[i+1][1] :
      temp=a[i]
      a[i]=a[i+1]
      a[i+1]=temp
for i in range(len(a)) :
   print(a[i])
