for _ in range(int(input())):
    n, a, b, c, d = map(int, input().split())
    s = a - b
    r = a + b
    s2 = c - d
    r2 = c + d
    if n * s > r2 or n * r < s2:
        print("NO")
    else:
        print("YES")
