# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
n = int(input())
names = []
for i in range(n):
    x = input()
    if x not in names:
        print("NO")
        names.append(x)
    else:
        print("YES")
