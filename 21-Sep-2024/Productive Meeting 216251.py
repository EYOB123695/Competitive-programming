# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq 
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    maxheap = []
    for idx,i in enumerate(arr):
        if i > 0:
            heapq.heappush(maxheap,(-i , idx + 1 ))

    ans = []
    
    while len(maxheap) > 1:
        curr, pos = heapq.heappop(maxheap) 
        currtwo , postwo = heapq.heappop(maxheap) 
        ans.append((pos,postwo))
        curr += 1 
        currtwo +=1 
        if curr != 0:
            heapq.heappush(maxheap,(curr, pos) )
        if currtwo !=0:
            heapq.heappush(maxheap,(currtwo, postwo) )


       
        


    
  
    

    print(len(ans))
    for k,l in ans:
        print(k,l,sep = " ")

    




