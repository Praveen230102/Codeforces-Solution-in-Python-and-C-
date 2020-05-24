n = int(input())
arr = list(input())
count = 0
remove = 0
for i in arr:
    if i == "x":
        if count >= 2:
            remove += 1
        else:
            count += 1
    else:
        count = 0
print(remove)
