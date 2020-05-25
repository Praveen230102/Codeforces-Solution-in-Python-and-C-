# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
s = input()
temp = s[0:-1]
temp1 = list(temp)
temp1.reverse()
s = list(s)
x = s + temp1
print("".join(x))
