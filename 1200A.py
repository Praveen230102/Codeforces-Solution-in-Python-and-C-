# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
s = list(input())
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, n):
    if s[i] == "L":
        temp = arr.index(0)
        arr[temp] = 1
    elif s[i] == "R":
        arr.reverse()
        temp = arr.index(0)
        arr[temp] = 1
        arr.reverse()
    elif s[i] == "1":
        arr[1] = 0
    elif s[i] == "2":
        arr[2] = 0
    elif s[i] == "3":
        arr[3] = 0
    elif s[i] == "4":
        arr[4] = 0
    elif s[i] == "5":
        arr[5] = 0
    elif s[i] == "6":
        arr[6] = 0
    elif s[i] == "7":
        arr[7] = 0
    elif s[i] == "8":
        arr[8] = 0
    elif s[i] == "9":
        arr[9] = 0
    elif s[i] == "0":
        arr[0] = 0
print(*arr, sep="")
