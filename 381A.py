# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
s = 0
d = 0
for i in range(0, n):
    if i % 2 == 0:
        temp = max(arr[0], arr[-1])
        s += temp
        arr.remove(temp)
    else:
        temp = max(arr[0], arr[-1])
        d += temp
        arr.remove(temp)
print(s, d)
