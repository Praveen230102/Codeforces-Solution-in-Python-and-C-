# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
d1, d2, d3 = map(int, input().split())
temp = 2 * d1 + 2 * d2
temp1 = d1 + d3 + d2
temp2 = 2 * d1 + 2 * d3
temp3 = 2 * d2 + 2 * d3
print(min(temp, temp1, temp2, temp3))
