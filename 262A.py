# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, k = map(int, input().split())
arr = list(map(str, input().split()))
count_ = 0
for i in arr:
    if (i.count("4") + i.count("7")) > k:
        continue
    else:
        count_ += 1
print(count_)
