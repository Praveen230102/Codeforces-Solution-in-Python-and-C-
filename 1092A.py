# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    new = ""
    rem = ""
    for j in range(k):
        new += alpha[j]
    # pahele length // frequency count kiya utna multiply kr ke add kr diya
    temp = n // k
    rem += new*temp
    r = n - (temp * k)
    # uske bad kitne bache hue hh length complete hone me
    # phir add kr dia
    for j in range(r):
        rem += new[j]
    print(rem)
