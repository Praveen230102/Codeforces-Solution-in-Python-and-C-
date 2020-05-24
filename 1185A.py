a, b, c, d = map(int, input().split())
new = []
new.append(a)
new.append(b)
new.append(c)
new = sorted(new)
count_ = 0
if new[1] - new[0] < d:
    count_ += d - (new[1] - new[0])
if new[2] - new[1] < d:
    count_ += d - (new[2] - new[1])
print(count_)
