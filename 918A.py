# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
from math import *
# from itertools import *
# import random
def isperfect(x):
    s = int(sqrt(x))
    return s*s == x


def is_fib(n):
    return isperfect(5*n*n + 4) or isperfect(5*n*n - 4)


rem = ""
n = int(input())
for i in range(1, n+1):
    if is_fib(i) == True:
        rem += "O"
    else:
        rem += "o"
print(rem)
