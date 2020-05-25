# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, k = map(int, input().split())
arr = list(input())
pos = arr.index("G")
target = arr.index("T")
if pos > target:
    flag = 0
    for i in range(pos, target - 1, -k):
        if arr[i] == "#":
            flag = 0
            break
        elif arr[i] == "T":
            flag = 1
            break
        else:
            continue
    if flag == 0:
        print("NO")
    else:
        print("YES")
else:
    flag = 0
    for i in range(pos, target + 1, k):
        if arr[i] == "#":
            flag = 0
            break
        elif arr[i] == "T":
            flag = 1
            break
        else:
            continue
    if flag == 0:
        print("NO")
    else:
        print("YES")
