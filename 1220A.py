n = int(input())
arr = list(input())
ones = 3
zeroes = 4
z1 = arr.count("z")
n1 = arr.count("n")
new = []
for i in range(n1):
    new.append("1")
for i in range(z1):
    new.append("0")
print(*new, sep=" ")
