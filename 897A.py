# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n, k = map(int, input().split())
s = list(input())
for i in range(k):
    l, r, c1, c2 = map(str, input().split())
    for j in range(int(l)-1, int(r)):
        if s[j] == c1:
            s[j] = c2
        else:
            continue
print("".join(s))
