# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
total_ = 0
if e > f:
    temp = min(a, d)
    total_ += e * temp
    a -= temp
    d -= temp
    temp1 = min(b, c, d)
    total_ += f * temp1
elif f >= e:
    temp = min(b, c, d)
    total_ += f * temp
    b -= temp
    c -= temp
    d -= temp
    temp1 = min(a, d)
    total_ += temp1 * e
print(total_)
