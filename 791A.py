a, b = map(int, input().split())
count = 0
for i in range(1, 1000000):
    if a > b:
        print(count)
        break
    else:
        a *= 3
        b *= 2
        count += 1
        continue
