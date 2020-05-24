import math
q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    print(int(math.ceil(sum(arr)/n)))
