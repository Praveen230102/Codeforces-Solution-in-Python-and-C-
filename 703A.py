n = int(input())
m = 0
c = 0
for i in range(n):
    mi, ch = map(int, input().split())
    if mi > ch:
        m += 1
    elif mi < ch:
        c += 1
    else:
        continue
if m > c:
    print("Mishka")
elif c > m:
    print("Chris")
else:
    print("Friendship is magic!^^")
