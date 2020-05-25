# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
ans = []
for i in arr:
    if i % 2 == 0:
        ans.append(i-1)
    else:
        ans.append(i)
print(*ans, sep=" ")
