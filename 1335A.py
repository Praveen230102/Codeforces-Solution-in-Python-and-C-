t = int(input())
for i in range(t):
    n = int(input())
    if n <= 2:
        print(0)
    else:
        hf = n // 2
        hf += 1
        print(n - hf)
