# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
count_ = 0
for i in range(1, n-1):
    if (arr[i] < arr[i-1] and arr[i] < arr[i+1]) or (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
        count_ += 1
    else:
        continue
print(count_)
