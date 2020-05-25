# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
s = list(input())
if len(s) == 1:
    print("".join(s))
else:
    if len(s) % 2 == 0:
        first = s[0: len(s) // 2]
        f = list(first)
        f.reverse()
        first = "".join(f)
        last = s[len(s) // 2:]
        rem = ""
        for i in range(len(s) // 2):
            rem += first[i]
            rem += last[i]
        print(rem)
    else:
        first = s[0: len(s) // 2]
        last = s[len(s) // 2 + 1:]
        f = list(first)
        f.reverse()
        first = "".join(f)
        rem = ""
        rem += s[len(s) // 2]
        for i in range(len(first)):
            rem += last[i]
            rem += first[i]
        print(rem)
