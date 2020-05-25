# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random


def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


n, k = map(int, input().split())
count_ = 0
if isprime(k) == False:
    print("NO")
else:
    for i in range(n + 1, k):
        # this part of code need to improvise
        if isprime(i) == True:
            print("NO")
            count_ = 1
            break
        else:
            # count_ += 1
            continue
    if count_ == 0:
        print("YES")
