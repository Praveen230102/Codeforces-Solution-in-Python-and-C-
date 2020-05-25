# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
y, b, r = map(int, input().split())
if y < b - 1:
    y = y
else:
    y = b - 1
if y < r - 2:
    y = y
else:
    y = r - 2
print((3 * y) + 3)
