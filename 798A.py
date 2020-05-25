# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
count_ = 0
s = input()
for i in range(0, len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        count_ += 1
    else:
        continue
if count_ == 0 and len(s) % 2 != 0:
    print("YES")
elif count_ == 1:
    print("YES")
else:
    print("NO")
