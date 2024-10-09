# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

from collections import * 
n = int(input())
arr = list(map(int,input().split()))
countodd = 0
counteven = 0 
for i in arr:
    if i % 2 == 0:
        counteven += 1

    else :
        countodd += 1 

if counteven != 0 and countodd != 0:
    arr.sort()
    
    print(" ".join(map(str,arr)))

else:

    print(" ".join(map(str,arr)))