# Problem: B - K-divisible Sum - https://codeforces.com/gym/540354/problem/B

 
from collections import *
import math
T= int(input())
 
for _  in range(T):
    n,k = map(int,input().split())
    if n>= k:
        print(1 if n % k == 0 else 2)
    else :
        k += (n - (n % k))
        print(math.ceil(k / n))
