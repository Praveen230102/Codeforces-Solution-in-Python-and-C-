import math
t = int(input())
for _ in range(t):
    a, b, c, d, k = map(int, input().split())
    a = math.ceil(a/c)
    b = math.ceil(b/d)
    if a + b <= k:
        print(a, b)
    else:
        print(-1)
