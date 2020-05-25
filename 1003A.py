# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
max_ = max(arr, key=arr.count)
print(arr.count(max_))
