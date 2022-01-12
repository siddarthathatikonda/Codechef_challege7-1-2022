#num1 , num2 = float(input()).split()
#num2 = float(input())

# printing the sum in float
#print(num1 + num2)
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print(x+y)


#print(t)
def kepler(a,b,c,d):
    k = pow(a, 2) / pow(c, 3)
    m = pow(b, 2) / pow(d, 3)
    # print(k,m)
    if k == m:
       return 1
    else:
       return 0

t = int(input())
for i in range(t):
    a, b, c, d = [int(x) for x in input().split()]
    #print(a,b,c,d)
    k=kepler(a,b,c,d)
    if k == 1:
        print("Yes")
    else:
        print("No")

