# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
a, b = map(int, input().split())
for i in range(1, 10000000000):
    if i % 2 == 0:
        if i > b:
            print("Valera")
            break
        else:
            b -= i
    else:
        if i > a:
            print("Vladik")
            break
        else:
            a -= i
