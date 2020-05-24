n = int(input())
arr = list(map(int, input().split()))
s = []
m = max(arr)
for i in arr:
    s.append(abs(m-i))
print(sum(s))
