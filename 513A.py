# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n1, n2, k1, k2 = map(int, input().split())
for i in range(10000000):
    if i % 2 == 0:
        if n1 == 0:
            print("Second")
            break
        else:
            n1 -= 1
    else:
        if n2 == 0:
            print("First")
            break
        else:
            n2 -= 1
