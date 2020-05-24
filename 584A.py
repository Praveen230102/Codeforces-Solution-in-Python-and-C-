n, t = map(int, input().split())
if t == 10:
    if n == 1:
        print(-1)
    else:
        print(1,end="")
        for i in range(0,n-1):
            print(0,end="")
else:
    for i in range(0, n):
        print(t,end="")
