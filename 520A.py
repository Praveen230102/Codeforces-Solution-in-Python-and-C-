n = int(input())
s = input()
if n < 26:
    print("NO")
else:
    s = s.upper()
    s = list(s)
    lst = dict.fromkeys(s)
    if len(lst) < 26:
        print("NO")
    elif len(lst) == 26:
        print("YES")
