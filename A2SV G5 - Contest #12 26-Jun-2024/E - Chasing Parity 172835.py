# Problem: E - Chasing Parity - https://codeforces.com/gym/517685/problem/E

from collections import *
n = int(input())
arr = list(map(int,input().split()))
graph  = defaultdict(list)
for i in range(n):
    if i + arr[i] < n:
        graph[i+arr[i]].append(i)
    if i - arr[i] >= 0:
        graph[i-arr[i]].append(i)
def bfs(start,end):
    visited  = set()
    val = [-1] * n
    queue = deque()
    for c in start:
        
        queue.append(c)
        val[c] = 0
        visited.add(c)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i  not in visited :
                val[i] = val[node] + 1 

                queue.append(i)
                visited.add(i)
    for cur in end:
        ans[cur] = val[cur]

odd = []
even = []

for i,val in enumerate(arr):
    if val % 2 != 0:
        odd.append(i)
    else:
        even.append(i)
ans = [-1] * n
bfs(odd,even)
bfs(even,odd)
print(*ans)





           