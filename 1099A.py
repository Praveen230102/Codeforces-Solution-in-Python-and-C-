# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
curr_w, curr_h = map(int, input().split())
u1, h1 = map(int, input().split())
u2, h2 = map(int, input().split())
for i in range(curr_h, -1, -1):
    curr_w += i
    if i == h1:
        curr_w -= u1
    if i == h2:
        curr_w -= u2
    if curr_w < 0:
        curr_w = 0
if curr_w < 0:
    print(0)
else:
    print(curr_w)
