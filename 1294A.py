t = int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())
    m = max(a, b, c)
    m1 = (m - a) + (m - b) + (m - c)
    if m1 > n:
        print("NO")
    elif m1 <= n:
        temp = n - m1
        if temp % 3 == 0:
            print("YES")
        else:
            print("NO")
