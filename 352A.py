# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
temp = arr.count(5)
temp1 = arr.count(0)
if temp >= 9 and temp1 > 0:
    for i in range(0, temp // 9):
        print("555555555", end="")
    for i in range(0, temp1):
        print("0", end="")
elif temp1 > 0:
    print("0")
else:
    print(-1)
