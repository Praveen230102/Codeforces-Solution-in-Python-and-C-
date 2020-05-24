arr = list(map(int, input().split()))
temp = sorted(arr)
ans = []
for i in range(0, len(temp) - 1):
    ans.append(temp[-1] - temp[i])
for i in ans:
    print(i, end=" ")
