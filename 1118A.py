q = int(input())
for _ in range(q):
    n, a, b = map(int, input().split())
    if 2*a < b:
        print(n*a)
    else:
        temp = n % 2
        print(temp * a + (n//2)*b)
