s = input()
t = list(input())
t.reverse()
t = "".join(t)
if s == t:
    print("YES")
else:
    print("NO")
