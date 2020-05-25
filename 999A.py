# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
n, k = map(int, input().split())
arr = list(map(int, input().split()))
if max(arr) <= k:
    print(n)
else:
    temp = arr.copy()
    temp.reverse()
    count_ = 0
    for i in arr:
        if i <= k:
            count_ += 1
        else:
            break
    for i in temp:
        if i <= k:
            count_ += 1
        else:
            break
    print(count_)
