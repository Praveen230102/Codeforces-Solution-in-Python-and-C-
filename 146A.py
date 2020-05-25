# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
s = list(input())
if "0" in s or "1" in s or "2" in s or "3" in s or "5" in s or "6" in s or "8" in s or "9" in s:
    print("NO")
else:
    first = s[0:n // 2]
    last = s[n // 2:]
    first_sum_ = 0
    last_sum_ = 0
    for i in first:
        first_sum_ += int(i)
    for i in last:
        last_sum_ += int(i)
    if first_sum_ == last_sum_:
        print("YES")
    else:
        print("NO")
