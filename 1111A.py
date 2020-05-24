s = list(input())
t = list(input())
vowels = ["a", "e", "i", "o", "u"]
if len(s) < len(t):
    print("NO")
elif len(s) > len(t):
    print("NO")
elif len(s) == len(t):
    flag = 0
    for i in range(0, len(s)):
        if s[i] in vowels and t[i] in vowels:
            continue
        elif s[i] not in vowels and t[i] not in vowels:
            continue
        elif s[i] in vowels and t[i] not in vowels:
            flag = 1
            break
        elif s[i] not in vowels and t[i] in vowels:
            flag = 1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
