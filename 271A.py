n = int(input())
for i in range(n+1, 90000):
    s = list(str(i))
    temp = 0
    for j in s:
        if s.count(j) == 1:
            temp += 1
            continue
        else:
            break
    if temp == len(str(i)):
        print(i)
        break
