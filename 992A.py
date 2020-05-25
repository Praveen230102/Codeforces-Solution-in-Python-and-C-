# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(dict.fromkeys(list(map(int, input().split()))))
if 0 in arr:
    arr.remove(0)
    print(len(arr))
else:
    print(len(arr))
