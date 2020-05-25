# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(input())
    if n < 11:
        print("NO")
    elif n == 11 and arr[0] != "8":
        print("NO")
    elif n == 11 and arr[0] == "8":
        print("YES")
    elif n > 11 and "8" not in arr:
        print("NO")
    elif n > 11 and "8" in arr:
        arr.reverse()
        # print(arr)
        temp = arr[10:]
        # print(temp)
        if "8" not in temp:
            print("NO")
        else:
            print("YES")
