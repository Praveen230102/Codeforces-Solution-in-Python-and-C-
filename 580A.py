n = int(input())
arr = list(map(int, input().split()))
nums = []
count = 1
for i in range(0, n):
    for j in range(i+1, n):
        if arr[i] <= arr[j]:
            count += 1
            break
        else:
            nums.append(count)
            count = 1
            break
nums.append(count)
print(max(nums))
