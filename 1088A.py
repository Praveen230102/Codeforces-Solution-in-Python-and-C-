# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
flag = 0
n = int(input())
for i in range(2, n+1):
    for j in range(1, n+1):
        if i % j == 0 and i * j > n and (i / j) < n:
            print(i, j)
            flag = 1
            break
        else:
            continue
    if flag == 1:
        break
    else:
        continue
else:
    print(-1)
