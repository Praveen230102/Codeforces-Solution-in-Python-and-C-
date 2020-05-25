# bsdk idhar kya dekhne ko aaya hai, khud kr!!!
# from math import *
# from itertools import *
# import random
t = int(input())
for i in range(t):
    n = int(input())
    necklace = list(map(int, input().split()))
    braclet = list(map(int, input().split()))
    sum1 = []
    # for checking the original thing
    for j in range(0, n):
        sum1.append(necklace[j] + braclet[j])
    if len(list(dict.fromkeys(sum1))) == len(sum1):
        print(*necklace, sep=" ")
        print(*braclet, sep=" ")
    else:
        sum1.clear()
        # for checking the sort of necklace
        temp = necklace.copy()
        temp.sort()
        for j in range(0, n):
            sum1.append(temp[j] + braclet[j])
        if len(list(dict.fromkeys(sum1))) == len(sum1):
            print(*temp, sep=" ")
            print(*braclet, sep=" ")
        else:
            sum1.clear()
            temp.clear()
            # for checking the sort of braclet
            temp = braclet.copy()
            temp.sort()
            for j in range(0, n):
                sum1.append(temp[j] + necklace[j])
            if len(list(dict.fromkeys(sum1))) == len(sum1):
                print(*necklace, sep=" ")
                print(*temp, sep=" ")
            else:
                sum1.clear()
                temp.clear()
                # for checking the sort of both
                temp = necklace.copy()
                temp.sort()
                temp1 = braclet.copy()
                temp1.sort()
                for j in range(0, n):
                    sum1.append(temp[j] + temp1[j])
                if len(list(dict.fromkeys(sum1))) == len(sum1):
                    print(*temp, sep=" ")
                    print(*temp1, sep=" ")
                else:
                    sum1.clear()
