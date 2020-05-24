gems = ["Power", "Time", "Space", "Soul", "Reality", "Mind"]
colours = ["purple", "green", "blue", "orange", "red", "yellow"]
n = int(input())
not_ = []
for i in range(n):
    x = input()
    not_.append(x)
gem = []
for i in range(0, len(colours)):
    if colours[i] not in not_:
        gem.append(gems[i])
    else:
        continue
print(len(gem))
for i in gem:
    print(i)
