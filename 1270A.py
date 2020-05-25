# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t = int(input())
for i in range(t):
    n, k1, k2 = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    if max(first) > max(second):
        print("YES")
    elif max(first) < max(second):
        print("NO")
