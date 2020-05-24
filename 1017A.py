t = int(input())
sum_ = []
for i in range(t):
    arr = list(map(int, input().split()))
    sum_.append(sum(arr))
thomas = sum_[0]
sum_ = sorted(sum_)
sum_.reverse()
print(sum_.index(thomas) + 1)
