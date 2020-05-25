# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
first = list(input())
second = list(input())
n = input()
rem = ""
for i in n:
    if i.isalpha():
        if i.lower() == i:
            temp = first.index(i.lower())
            x = second[temp]
            rem += x
        elif i.lower() != i:
            temp = first.index(i.lower())
            x = second[temp]
            rem += x.upper()
    else:
        rem += i
print(rem)
