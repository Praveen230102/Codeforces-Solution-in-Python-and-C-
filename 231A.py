# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
t = int(input())
count_ = 0
for i in range(t):
    arr = list(map(int, input().split()))
    if arr.count(1) >= 2:
        count_ += 1
    else:
        continue
print(count_)
