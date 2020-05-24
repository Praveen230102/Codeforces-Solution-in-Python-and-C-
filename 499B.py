n, m = map(int, input().split())
first = []
sec = []
for i in range(m):
    l, r = map(str, input().split())
    first.append(l)
    sec.append(r)
all_ = input()
lst = all_.split(" ")
rem = []
for j in range(0, len(lst)):
    if lst[j] in first:
        x = first.index(lst[j])
        if len(sec[x]) < len(first[x]):
            rem.append(sec[x])
        else:
            rem.append(first[x])
    elif lst[j] in sec:
        x = sec.index(lst[j])
        if len(first[x]) < len(sec[x]):
            rem.append(first[x])
        elif len(first[x]) > len(sec[x]):
            rem.append(sec[x])
        else:
            rem.append(first[x])
print(" ".join(rem))
