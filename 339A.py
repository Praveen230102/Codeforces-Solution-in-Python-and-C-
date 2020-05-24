s = input()
if len(s) == 1:
    print(s)
else:
    arr = s.split("+")
    arr = sorted(arr)
    print("+".join(arr))
