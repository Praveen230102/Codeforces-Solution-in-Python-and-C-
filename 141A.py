s1 = list(input())
s2 = list(input())
s3 = list(input())
s1 += s2
if len(s3) < len(s1):
    print("NO")
else:
    count = 0
    for i in s3:
        if i in s1:
            s1.remove(i)
            count += 1
    if len(s1) == 0 and len(s3) == count:
        print("YES")
    elif len(s1) == 0 and len(s3) != count:
        print("NO")
    else:
        print("NO")
