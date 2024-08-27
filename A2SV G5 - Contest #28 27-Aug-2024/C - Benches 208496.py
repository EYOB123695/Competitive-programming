# Problem: C - Benches - https://codeforces.com/gym/540354/problem/C

from heapq import *
n = int(input())
m = int(input())
arr = [ ]
for i in range(n):

    arr.append(int(input()))
anstwo =  max(arr) + m
heapify(arr)
for i in range(m):
    x = heappop(arr)
    heappush(arr,x+1)
ansone = max(arr)
print(ansone,anstwo , sep =" ")



