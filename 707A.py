n, m = map(int, input().split())
flag = 0
for i in range(n):
    arr = list(map(str, input().split()))
    if "C" in arr or "M" in arr or "Y" in arr:
        flag = 1
    else:
        continue
if flag == 1:
    print("#Color")
elif flag == 0:
    print("#Black&White")
