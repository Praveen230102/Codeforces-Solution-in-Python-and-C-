s = input()
if s.upper() == s:
    print(s.lower())
elif s[0].lower() + s[1:].upper() == s:
    print(s.swapcase())
else:
    print(s)
