q = int(input())
for _ in range(q):
    a, b, k = map(int, input().split())
    if k % 2 == 0:
        odd = k // 2
        even = k // 2
        ts = (a*odd) - (b*even)
        print(ts)
    else:
        odd = k//2 + 1
        even = k - odd
        ts = (a * odd) - (b * even)
        print(ts)
