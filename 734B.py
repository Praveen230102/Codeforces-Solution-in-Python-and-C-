# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
k2, k3, k5, k6 = map(int, input().split())
temp = min(k2, k5, k6)
k2 -= temp
k5 -= temp
k6 -= temp
total_ = temp * 256
temp1 = min(k2, k3)
total_ += 32*temp1
print(total_)
