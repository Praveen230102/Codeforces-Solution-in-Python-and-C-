n = int(input())
arr = list(map(int, input().split()))
cops = 0
thief = 0
for i in arr:
    if i < 0 and cops == 0:
        thief += 1
    elif i > 0:
        cops += i
    elif (i < 0) and (cops > 0):
        cops -= 1
print(thief)
