# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, m = map(int, input().split())
nums = []
for i in range(m):
    x = input()
    if "0" in x:
        nums.append(1)
    else:
        nums.append(0)
count_ = []
for i in range(0, len(nums)):
    if nums[i] == 0:
        continue
    else:
        temp = 0
        for j in range(i, len(nums)):
            if nums[j] == 1:
                temp += 1
            else:
                break
        count_.append(temp)
if len(count_) == 0:
    print(0)
else:
    print(max(count_))
