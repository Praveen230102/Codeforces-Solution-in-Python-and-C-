n = int(input())
arr = list(map(int, input().split()))
temp = sorted(arr)
if arr == temp:
    print(*arr, sep=" ")
else:
    # now we have to write code
    # adding from last and updating the next ones
    temp = arr
    temp.reverse()
    for i in range(0, len(temp)):
        for j in range(i+1, len(temp)):
            if temp[j] <= temp[i]:
                continue
            else:
                x = temp[j] - temp[i]
                temp[i] += x
                temp[j] -= x
    temp.reverse()
    print(*temp, sep=" ")
