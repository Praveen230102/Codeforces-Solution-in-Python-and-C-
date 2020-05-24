t = int(input())
for i in range(t):
    hh, mm = map(int, input().split())
    h = 24 - hh
    print(h*60 - mm)
