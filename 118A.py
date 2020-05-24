s = input()
s = list(s.lower())
vo = ["a", "o", "y", "e", "u", "i"]
new = []
for i in s:
    if i not in vo:
        new.append(".")
        new.append(i)
print("".join(new))
