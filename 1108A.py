# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
for i in range(n):
    flag = 0
    l1, r1, l2, r2 = map(int, input().split())
    for j in range(l1, r1 + 1):
        for k in range(l2, r2 + 1):
            if j != k:
                print(j, k)
                flag = 1
                break
        if flag == 1:
            break
        else:
            continue
