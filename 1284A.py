n, m = map(int, input().split())
first = input()
arr = first.split(" ")
sec = input()
arr1 = sec.split(" ")
q = int(input())
for i in range(q):
    x = int(input())
    rem = ""
    if x <= n and x <= m:
        rem += arr[x-1]
        rem += arr1[x-1]
        print(rem)
    elif n < x <= m:
        temp = x % n
        rem += arr[temp - 1]
        rem += arr1[x-1]
        print(rem)
    elif n >= x > m:
        temp = x % m
        rem += arr[x-1]
        rem += arr1[temp - 1]
        print(rem)
    else:
        temp1 = x % n
        temp2 = x % m
        rem += arr[temp1 - 1]
        rem += arr1[temp2 - 1]
        print(rem)
