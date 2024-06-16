# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

import heapq
n = int(input())
arr = list(map(int,input().split()))
heap = []
sum = 0
for i in arr:
    sum += i 
    heapq.heappush(heap,i)
    while sum < 0:
        sum -= heapq.heappop(heap)

print(len(heap))