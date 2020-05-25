# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = list(input())
if n[-1] == 0:
    print("".join(n))
elif int(n[-1]) <= 5:
    n[-1] = "0"
    print("".join(n))
else:
    temp = int("".join(n))
    if n[-1] == "9":
        print(temp + 1)
    elif n[-1] == "8":
        print(temp + 2)
    elif n[-1] == "7":
        print(temp + 3)
    elif n[-1] == "6":
        print(temp + 4)
