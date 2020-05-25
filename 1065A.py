# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t = int(input())
for i in range(t):
    s, a, b, c = map(int, input().split())
    total_ = 0
    x = s // c
    temp = x // a
    total_ += x
    total_ += temp * b
    print(total_)
