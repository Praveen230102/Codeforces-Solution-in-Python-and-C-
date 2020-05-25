# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
pos = m - 1
if pos == 0:
    dis = 0
    for i in range(1, n):
        if arr[i] == 0:
            dis += 10
            continue
        elif arr[i] > k:
            dis += 10
            continue
        elif arr[i] <= k:
            dis += 10
            break
    print(dis)
else:
    dis1 = 0
    dis = 0
    flag = 0
    flag1 = 0
    for i in range(pos - 1, -1, -1):
        if arr[i] == 0:
            dis += 10
            continue
        elif arr[i] > k:
            dis += 10
            continue
        elif arr[i] <= k:
            dis += 10
            flag = 1
            break
    for i in range(pos + 1, n):
        if arr[i] == 0:
            dis1 += 10
            continue
        elif arr[i] > k:
            dis1 += 10
            continue
        elif arr[i] <= k:
            dis1 += 10
            flag1 = 1
            break
    if flag == 1 and flag1 == 0:
        print(dis)
    elif flag == 0 and flag1 == 1:
        print(dis1)
    elif flag == 1 and flag == 1:
        print(min(dis, dis1))
