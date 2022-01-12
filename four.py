t = int(input())
lst =[]
for i in range(0,t):
    k=input()
    m=len(k)
    count=0
    for j in range(0,m):
        if k[j] == '4':
            count = count+1
    print(count)