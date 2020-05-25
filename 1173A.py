# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
x, y, z = map(int, input().split())
if z == 0:
    if x > y:
        print("+")
    elif x == y:
        print("0")
    else:
        print("-")
else:
    if x > y:
        if (x - y) > z:
            print("+")
        elif (x - y) <= z:
            print("?")
    elif y > x:
        if (y - x) > z:
            print("-")
        elif (y - x) <= z:
            print("?")
    else:
        print("?")
