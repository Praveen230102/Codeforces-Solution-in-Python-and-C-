t = int(input())
for i in range(t):
    x = input()
    if x.endswith("po"):
        print("FILIPINO")
    elif x.endswith("desu") or x.endswith("masu"):
        print("JAPANESE")
    elif x.endswith("mnida"):
        print("KOREAN")
