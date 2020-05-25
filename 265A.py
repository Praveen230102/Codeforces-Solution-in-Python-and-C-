# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
s = list(input())
t = list(input())
count_ = 0
for i in range(0, len(t)):
    if s[count_] == t[i]:
        count_ += 1
    else:
        continue
print(count_ + 1)
