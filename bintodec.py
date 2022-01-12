str = input()
k = len(str)
res = 0
lst=[]
for i in range(k):
  m = int(str[k-1-i])
  lst.append(m)
n=len(lst)
j = 0
x = 0
for i in lst:
  x = x+(i*pow(2, j))
  if j < n:
    j +=1

print(x)
