n = int(input())
s = input()
sf = 0
fs = 0
flag = 0
for i in range(0, n):
    for j in range(i+1, n):
        if s[i] == "S" and s[j] == "F":
            sf += 1
            flag = 1
            break
        elif s[i] == "F" and s[j] == "S":
            fs += 1
            flag = 1
            break
        else:
            flag = 1
            break
if sf > fs:
    print("YES")
else:
    print("NO")
