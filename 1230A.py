# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
arr = list(map(int, input().split()))
arr.sort()
if arr[3] == arr[0] + arr[1] + arr[2]:
    print("YES")
elif arr[0] + arr[3] == arr[1] + arr[2]:
    print("YES")
else:
    print("NO")
