# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
odd_arr = []
even_arr = []
odd_arr1 = []
even_arr1 = []
for i in arr:
    if i % 2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)
for i in arr1:
    if i % 2 == 0:
        even_arr1.append(i)
    else:
        odd_arr1.append(i)
print(min(len(odd_arr), len(even_arr1)) + min(len(even_arr), len(odd_arr1)))
