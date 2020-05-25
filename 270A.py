# idhar kya dekhne ko aaya hai!!!!!!!!
t = int(input())
for i in range(t):
    x = int(input())
    if 360 % (180 - x) == 0:
        print("YES")
    else:
        print("NO")
