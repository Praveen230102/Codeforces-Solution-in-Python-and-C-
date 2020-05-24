n = input()
if int(n) >= 0:
    print(n)
else:
    s = list(n)
    s.remove("-")
    temp = s.copy()
    temp.pop(-2)
    x = int("".join(temp))
    s.pop(-1)
    y = int("".join(s))
    if -1*x > -1*y:
        print(-1*x)
    else:
        print(-1*y)
 
