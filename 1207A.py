# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
t = int(input())
for i in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if b <= 1:
        print(0)
    elif b > 1:
        b = b // 2
        if c >= h:
            total_ = 0
            min_ = min(b, f)
            total_ += min_ * c
            b -= min_
            min_ = min(b, p)
            total_ += min_ * h
            print(total_)
        elif h > c:
            total_ = 0
            min_ = min(b, p)
            total_ += min_ * h
            b -= min_
            min_ = min(b, f)
            total_ += min_ * c
            print(total_)
