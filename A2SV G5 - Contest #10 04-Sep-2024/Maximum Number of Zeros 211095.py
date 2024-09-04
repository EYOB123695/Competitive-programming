# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

 
from collections import Counter
from math import gcd
n = int(input().strip())
arr = list(map(int,input().split()))
 
arrtwo  = list(map(int,input().split()))
count = Counter()
ans = 0  
for i in range(n):
    if arr[i] == 0:
        if arrtwo[i] == 0:
            ans += 1
    else:
       
        x = arrtwo[i] // (gcd(abs(arr[i]), abs(arrtwo[i])))
        y = arr[i] // (gcd(abs(arr[i]), abs(arrtwo[i])))
        if arrtwo[i] < 0:
            x *=  -1
            y *= -1
        elif arrtwo[i] == 0 and arr[i] < 0:
            y *=  -1
        count[(x, y)] += 1
if len(count) == 0:
    print(ans)
else:
    print(ans + max(count.values())) 