s = input()
lst = []
for i in s:
    if i == "{" or i == "}" or i == "," or i == " ":
        pass
    else:
        lst.append(i)
print(len(list(dict.fromkeys(lst))))
