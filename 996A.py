# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
total_ = 0
nums = [100, 20, 10, 5, 1]
for i in nums:
    if n // i != 0:
        total_ += n // i
        n %= i
    else:
        continue
print(total_)
