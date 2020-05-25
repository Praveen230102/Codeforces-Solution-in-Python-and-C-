# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
cd = input()
col = cd[0]
row = int(cd[-1])
if col == "a" or col == "h":
    if row == 1 or row == 8:
        print(3)
    else:
        print(5)
elif col == "b" or col == "c" or col == "d" or col == "e" or col == "f" or col == "g":
    if row == 1 or row == 8:
        print(5)
    else:
        print(8)
