a, b = map(int, input().split())
if a < b:
    temp = b - a
    print(a, temp // 2)
elif b < a:
    temp = a - b
    print(b, temp // 2)
elif a == b:
    print(a, 0)
