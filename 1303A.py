t = int(input())
for i in range(t):
    arr = list(input())
    if "1" not in arr:
        print(0)
    else:
        first_att = arr.index("1")
        temp = arr[:]
        temp.reverse()
        last_att = len(temp) - temp.index("1") - 1
        count = 0
        for j in range(first_att, last_att):
            if arr[j] == "0":
                count += 1
            else:
                continue
        print(count)
 
