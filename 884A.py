# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t, m = map(int, input().split())
arr = list(map(int, input().split()))
count_ = 0
for i in arr:
    temp = 86400 - i
    if m == 0:
        break
    else:
        m -= temp
        count_ += 1
        if m <= 0:
            m = 0
        else:
            continue
print(count_)
