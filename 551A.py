# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
n = int(input())
arr = list(map(int, input().split()))
temp = arr.copy()
temp.sort()
temp.reverse()
standing = []
curr = temp[0]
position = 1
standing.append(position)
for i in range(1, len(temp)):
    if temp[i] == curr:
        standing.append(position)
    else:
        standing.append(i + 1)
        curr = temp[i]
        position = i
for i in range(0, n):
    if arr[i] in temp:
        x = temp.index(arr[i])
        print(standing[x], end=" ")
