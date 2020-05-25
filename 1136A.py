# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t = int(input())
pages = []
for i in range(t):
    l, r = map(int, input().split())
    pages.append(r)
k = int(input())
for i in pages:
    if k <= i:
        print(len(pages) - pages.index(i))
        break
    else:
        continue
