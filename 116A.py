n = int(input())
total = 0
min_ = 0
for i in range(n):
    a, b = map(int, input().split())
    total -= a
    total += b
    if total > min_:
        min_ = total
    else:
        continue
print(min_)
