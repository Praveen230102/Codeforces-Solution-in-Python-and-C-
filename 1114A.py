# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
x, y, z = map(int, input().split())
a, b, c = map(int, input().split())
flag = 1
if x > a:
    print("NO")
    flag = 0
elif x <= a:
    flag = 1
    a -= x
    if y > a + b:
        print("NO")
        flag = 0
    elif y <= a + b:
        flag = 1
        total_ = a+b
        total_ -= y
        if z > total_ + c:
            print("NO")
            flag = 0
        elif z <= total_ + c:
            print("YES")
