# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
import random
n = int(input())
arr = list(map(int, input().split()))
point = max(arr)
e_s = sum(arr)
for i in range(max(arr), 1000000000):
    a_s = 0
    for j in range(0, n):
        a_s += abs(arr[j] - i)
    if a_s > e_s:
        print(i)
        break
    else:
        continue
