n, k = map(int, input().split())
if n == 1:
    print("YES")
else:
    if (n // k) % 2 != 0:
        print("YES")
    else:
        print("NO")
