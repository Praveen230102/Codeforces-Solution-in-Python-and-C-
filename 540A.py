# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = 10
x = int(input())
s = input()
s1 = input()
total_ = 0
for i in range(0, x):
    temp = int(s[i]) - int(s1[i])
    if temp < 0:
        temp = -temp
    if temp > (n // 2):
        temp = n - temp
    total_ += temp
print(total_)
