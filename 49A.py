# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
vowel = ["a", "e", "i", "o", "u", "y"]
s = list(input())
s.reverse()
for i in s:
    if i.isalpha():
        if i.lower() in vowel:
            print("YES")
            break
        else:
            print("NO")
            break
    else:
        continue
