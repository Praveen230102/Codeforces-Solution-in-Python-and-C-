# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
t = int(input())
rem = []
for i in range(0, 3):
    rem.append((t + i) % 4)
if 1 in rem:
    print(rem.index(1), "A")
elif 3 in rem:
    print(rem.index(3), "B")
elif 2 in rem:
    print(rem.index(2), "C")
elif 0 in rem:
    print(rem.index(0), "D")
