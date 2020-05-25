# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t = int(input())
arr = list(map(int, input().split()))
arr.sort()
new_arr = list(dict.fromkeys(arr))
if len(new_arr) == 1:
    print("NO")
else:
    if new_arr[1] == 101:
        print("NO")
    else:
        print(new_arr[1])
