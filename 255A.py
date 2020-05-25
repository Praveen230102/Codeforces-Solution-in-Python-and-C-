# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
chest = 0
bis = 0
back = 0
for i in range(0, n, 3):
    chest += arr[i]
for i in range(1, n, 3):
    bis += arr[i]
for i in range(2, n, 3):
    back += arr[i]
if max(chest, bis, back) == chest:
    print("chest")
elif max(chest, bis, back) == bis:
    print("biceps")
else:
    print("back")
