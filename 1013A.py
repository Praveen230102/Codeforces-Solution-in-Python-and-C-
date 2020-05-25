# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
if sum(arr1) <= sum(arr):
    print("Yes")
else:
    print("No")
