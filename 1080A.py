import math
n, k = map(int, input().split())
red = 2
green = 5
blue = 8
sum_ = math.ceil((red*n)/k) + math.ceil((green*n)/k) + math.ceil((blue*n)/k)
print(sum_)
