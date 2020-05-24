n = int(input())
arr = list(input())
nums = []
for i in range(0, n):
    for j in range(i+1, n):
        nums.append(arr[i]+arr[j])
        break
print(max(nums, key=nums.count))
