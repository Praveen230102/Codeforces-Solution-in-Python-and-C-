# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
from math import *
# from itertools import *
# import random
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())
t_c = a1 + a2 + a3
t_m = b1 + b2 + b3
if int(ceil(t_c / 5)) + int(ceil(t_m / 10)) > n:
    print("NO")
else:
    print("YES")
