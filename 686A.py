# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, init = map(int, input().split())
count_ = 0
for i in range(n):
    arr = list(map(str, input().split()))
    if arr[0] == "+":
        init += int(arr[1])
    else:
        if int(arr[1]) <= init:
            init -= int(arr[1])
        else:
            count_ += 1
print(init, count_)
