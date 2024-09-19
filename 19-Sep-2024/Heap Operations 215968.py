# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from collections import * 
import heapq
n = int(input())
arr = []
for i in range(n):
    x = input()
    arr.append(x)
x = []
heapq.heapify(x)
ans = []
for i in arr:
    if  i[0] == "i" :
        
        h,y = i.split()
        y  = int(y)
        heapq.heappush(x,y)
        ans.append(i)

    elif i[0] == "g":
        z,k = i.split()
        k = int(k)
        while x and x[0] <k:
            heapq.heappop(x)
            ans.append("removeMin")
        if not x or x[0] > k:
            heapq.heappush(x,k) 
            ans.append(f"insert {k}")
        ans.append(i)
        
    else:
        
        if not x:
            ans.append("insert 0")
            heapq.heappush(x,0) 

        heapq.heappop(x)
        ans.append(i) 
print(len(ans))
for j in ans:
    print(j)


