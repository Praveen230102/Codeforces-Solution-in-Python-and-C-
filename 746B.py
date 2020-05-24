n = int(input())
arr = list(input())
if n % 2 != 0:
    output = []
    for i in range(0, len(arr)):
        if i % 2 == 0:
            output.append(arr[i])
        else:
            output.insert(0, arr[i])
    print("".join(output))
else:
    output = []
    for i in range(0 , len(arr)):
        if i % 2 == 0:
            output.insert(0, arr[i])
        else:
            output.append(arr[i])
    print("".join(output))
