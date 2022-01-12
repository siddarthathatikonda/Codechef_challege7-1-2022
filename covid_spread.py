

# def covid(a, b):
#     x = 0
#     for i in range(0,b+1):
#         print("this is for ",i)
#         if i <= 10 and a-x >= 0:
#             x = 2**i
#             print("i less than or equal to 10",x)
#         elif i > 10 and a-x >= 0:
#             x = x*3
#             print("i greater than or equal to 11",x)
#         else:
#             if x > a:
#                 return a
#
#     else:
#         if x > a:
#             x = x//3
#             return x
#         else:
#             return x
#
# t= int(input())
# for e in range(t):
#     a, b = [int(x) for x in input().split()]
#     k = covid(a, b)
#     print(k)


def covid(a, b):
    x = 0
    for i in range(b+1):
        if i <= 10 and a-x > 0:
            x = pow(2,i)
        elif i > 10 and a-x > 0:
            x = x*3
        else:
            if x > a:
                return a

    else:
        if x > a:
            return a
        else:

            return x
t= int(input())
for e in range(t):
    a, b = [int(x) for x in input().split()]
    k = covid(a, b)
    print(k)