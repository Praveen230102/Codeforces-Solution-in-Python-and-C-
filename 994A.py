# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m = map(int, input().split())
arr = list(map(int, input().split()))
finger = list(map(int, input().split()))
ans = []
for i in arr:
    if i in finger:
        ans.append(i)
    else:
        continue
if len(ans) == 0:
    print("")
else:
    print(*ans, sep=" ")
