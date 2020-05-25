# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
index_ = []
for i in arr:
    check_with = arr.index(i) + 1
    temp = arr[i - 1]
    check_for = arr[temp - 1]
    if check_for == check_with:
        print("YES")
        break
    else:
        continue
else:
    print("NO")
