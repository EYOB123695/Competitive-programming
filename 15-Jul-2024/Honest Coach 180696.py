# Problem: Honest Coach - https://codeforces.com/problemset/problem/1360/B

import math
T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
   
    
    arr.sort() 
    ans = []
    diff = float("inf")

    for i in range(len(arr)-1):
         
        diff = min(diff,arr[i+1] -arr[i])
    print(diff)



           


 