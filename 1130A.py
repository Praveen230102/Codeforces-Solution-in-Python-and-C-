# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
temp = int(ceil(n / 2))
if sum(arr) >= 0:
    for i in range(-1000, 1001, 1):
        if i == 0:
            continue
        else:
            new = []
            for j in arr:
                new.append(j / i)
            pos_count = 0
            for j in new:
                if j > 0:
                    pos_count += 1
            if pos_count >= temp:
                print(i)
                break
            else:
                continue
    else:
        print(0)
else:
    for i in range(-1000, 1001, 1):
        if i == 0:
            continue
        else:
            new = []
            for j in arr:
                new.append(j / i)
            pos_count = 0
            for j in new:
                if j > 0:
                    pos_count += 1
            if pos_count >= temp:
                print(i)
                break
            else:
                continue
    else:
        print(0)
