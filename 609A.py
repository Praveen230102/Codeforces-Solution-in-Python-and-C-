# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
m = int(input())
USB = []
for i in range(n):
    USB.append(int(input()))
USB.sort()
total_ = 0
USB.reverse()
for i in range(0, len(USB)):
    if m > 0:
        total_ += 1
        m -= USB[i]
    else:
        break
print(total_)
