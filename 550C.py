import itertools as it

n = list(input())
flag = 0
for i in range(1, 4):
    temp = it.combinations(n, i)
    for j in temp:
        temp1 = int(''.join(j))
        if temp1 % 8 == 0:
            print("YES")
            print(temp1)
            flag = 1
            break
        else:
            continue
    if flag == 1:
        break
if flag != 1:
    print("NO")
