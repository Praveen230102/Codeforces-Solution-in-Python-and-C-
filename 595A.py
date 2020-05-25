# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m = map(int, input().split())
total_ = 0
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(0, len(arr), 2):
        if arr[j] == 1 or arr[j+1] == 1:
            total_ += 1
        else:
            continue
print(total_)
