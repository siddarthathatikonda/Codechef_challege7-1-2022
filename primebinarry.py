def substrings(s, n):
    lst1 = []
    for i in range(n):
        temp = ""
        for j in range(i, n):
            temp += s[j]
            lst1.append(temp)
    print(lst1)
    for e in lst1:
        k = len(e)
        res = 0
        lst = []
        for i in range(k):
            m = int(e[k - 1 - i])
            lst.append(m)
        n = len(lst)
        j = 0
        x = 0
        for i in lst:
            x = x + (i * pow(2, j))
            if j < n:
                j += 1
        if x == 2 or x==3 or x==5 or x==7 or x==11 :
            print("Yes")
            break
    else :
        print("No")



t=int(input())
for k in range(t+1):
   s = input()
   substrings(s, len(s))













