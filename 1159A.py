# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
s = list(input())
count_ = 0
min_ = 0
for i in range(0, n):
    count_ += (s[i] == "+") - (s[i] == "-")
    if min_ < count_:
        max_ = min_
    else:
        min_ = count_
print(count_ - min_)
