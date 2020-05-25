# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
arr = list(input())
count_ = 0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] == "Q" and arr[j] == "A" and arr[k] == "Q":
                count_ += 1
            else:
                continue
print(count_)
