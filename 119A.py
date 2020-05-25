# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
from math import *
# from itertools import *
# import random
a, b, n = map(int, input().split())
for i in range(100000000):
    if i % 2 == 0:
        temp = gcd(a, n)
        if temp > n:
            print(1)
            break
        else:
            n -= temp
    elif i % 2 != 0:
        temp = gcd(b, n)
        if temp > n:
            print(0)
            break
        else:
            n -= temp
