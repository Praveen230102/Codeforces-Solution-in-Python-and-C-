# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
arr = list(map(int, input().split()))
arr.sort()
if arr[0] + arr[1] > arr[2]:
    print(0)
elif arr[0] + arr[1] <= arr[2]:
    temp = arr[0] + arr[1]
    print(arr[2] - temp + 1)
