# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
t = int(input())
arr = list(map(int, input().split()))
min_ = arr[0]
count_ = 0
max_ = arr[0]
for i in range(0, t):
    if arr[i] > max_:
        count_ += 1
        max_ = arr[i]
    elif arr[i] < min_:
        min_ = arr[i]
        count_ += 1
    elif min_ <= arr[i] <= max_:
        continue
print(count_)
