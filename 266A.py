n = int(input())
s = list(input())
count = 0
for i in range(0, n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            count += 1
            break
        else:
            break
print(count)
