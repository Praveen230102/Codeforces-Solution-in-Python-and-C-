# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t = int(input())
flag = 0
for i in range(t):
    name, before, after = map(str, input().split())
    if int(before) >= 2400 and (int(after) > int(before)):
        flag += 1
    else:
        continue
if flag > 0:
    print("YES")
else:
    print("NO")
