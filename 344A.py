n = int(input())
magnets = []
for i in range(n):
    x = input()
    magnets.append(x)
count_ = 1
for i in range(0, n):
    for j in range(i+1, n):
        if magnets[i] == magnets[j]:
            break
        else:
            count_ += 1
            break
print(count_)
