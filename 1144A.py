all_ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
q = int(input())
for i in range(q):
    arr = list(input())
    arr1 = sorted(arr)
    first = min(arr1)
    last = max(arr1)
    x1 = all_.index(first)
    x2 = all_.index(last)
    flag = 0
    new = []
    for j in range(x1, x2 + 1):
        new.append(all_[j])
    if new == arr1:
        print("YES")
    else:
        print("NO")
