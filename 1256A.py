q = int(input())
for i in range(q):
    a, b, n, s = map(int, input().split())
    total = a*n + b
    if s > total:
        print("NO")
    else:
        temp = s // n
        s -= (temp*n)
        if s > b:
            print("NO")
        elif s <= b:
            print("YES")
