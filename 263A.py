r1 = input()
r1 = r1.split(" ")
r2 = input()
r2 = r2.split(" ")
r3 = input()
r3 = r3.split(" ")
r4 = input()
r4 = r4.split(" ")
r5 = input()
r5 = r5.split(" ")
ini_row = 3
ini_col = 3
col = 0
row = 0
if "1" in r1:
    col = 1
    row = r1.index("1") + 1
    print(abs(ini_col - col) + abs(ini_row - row))
    # print(col, row)
elif "1" in r2:
    col = 2
    row = r2.index("1") + 1
    print(abs(ini_col - col) + abs(ini_row - row))
    # print(col, row)
elif "1" in r3:
    col = 3
    row = r3.index("1") + 1
    print(abs(ini_col - col) + abs(ini_row - row))
    # print(col, row)
elif "1" in r4:
    col = 4
    row = r4.index("1") + 1
    print(abs(ini_col - col) + abs(ini_row - row))
    # print(col, row)
elif "1" in r5:
    col = 5
    row = r5.index("1") + 1
    print(abs(ini_col - col) + abs(ini_row - row))
    # print(col, row)
