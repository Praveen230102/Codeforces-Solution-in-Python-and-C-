# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
import random
n, k = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = list(dict.fromkeys(arr))
if k > len(new_arr):
    print("NO")
else:
    index_ = []
    temp = random.sample(new_arr, k)
    for i in temp:
        index_.append(arr.index(i) + 1)
    print("YES")
    print(*index_, sep=" ")
