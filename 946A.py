# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
b = []
c = []
for i in arr:
    if i < 0:
        c.append(i)
    else:
        b.append(i)
print(sum(b) - sum(c))
