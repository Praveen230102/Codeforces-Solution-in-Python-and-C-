# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m = map(int, input().split())
total_ = 0
for i in range(0, max(n, m) + 1):
    for j in range(0, max(n, m) + 1):
        if ((i*i) + j == n) and (i + (j*j) == m):
            total_ += 1
        else:
            continue
print(total_)
