# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m = map(int, input().split())
temp = n * (n + 1) // 2
for i in range(100000000):
    if temp <= m:
        m -= temp
    elif temp > m:
        break
if m == 0:
    print(0)
else:
    for i in range(1, n + 1):
        if m >= i:
            m -= i
        elif m < i:
            print(m)
            break
