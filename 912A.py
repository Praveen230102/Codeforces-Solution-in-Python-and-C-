# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
a, b = map(int, input().split())
x, y, z = map(int, input().split())
u = 2 * x + y
v = y + 3 * z
if a < u:
    temp = u - a
else:
    temp = 0
if b < v:
    temp1 = v - b
else:
    temp1 = 0
print(temp + temp1)
