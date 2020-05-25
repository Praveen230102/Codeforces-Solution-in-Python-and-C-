# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random


def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
for j in range(1, 1000):
    temp = n * j + 1
    if not prime(temp):
        print(j)
        break
    else:
        continue
