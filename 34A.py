# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
first = n
sec = 1
# diff.append(abs(arr[0] - arr[-1]))
temp = abs(arr[0] - arr[-1])
for i in range(0, n):
    for j in range(i+1, n):
        if abs(arr[i] - arr[j]) < temp:
            temp = abs(arr[i] - arr[j])
            first = i + 1
            sec = j + 1
            break
        else:
            break
print(first, sec)
