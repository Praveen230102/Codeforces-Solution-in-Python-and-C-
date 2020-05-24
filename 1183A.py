n = int(input())
for i in range(n, 1000000):
    temp = list(str(i))
    sum_ = 0
    for j in temp:
        sum_ += int(j)
    if sum_ % 4 == 0:
        print(i)
        break
    else:
        continue
