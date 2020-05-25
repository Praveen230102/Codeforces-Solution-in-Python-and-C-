# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
l, r, a = map(int, input().split())
if a == 0:
    min_ = min(l, r)
    print(2 * min_)
elif a != 0:
    # a is not equal to zero then we have to check if its diff is less than or equal or a or not and then we have to
    # check the same for another case
    if l < r:
        if r - l >= a:
            l += a
            print(2 * min(l, r))
        elif r - l < a:
            temp = r - l
            l += temp
            a -= temp
            x = a // 2
            l += x
            r += x
            print(2 * min(l, r))
    elif l > r:
        if l - r >= a:
            r += a
            print(2 * min(l, r))
        elif l - r < a:
            temp = l - r
            r += temp
            a -= temp
            x = a // 2
            l += x
            r += x
            print(2 * min(l, r))
    else:
        temp = a // 2
        l += temp
        r += temp
        print(2 * min(l, r))
