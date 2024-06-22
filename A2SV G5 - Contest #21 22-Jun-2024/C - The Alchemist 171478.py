# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C


from collections import *

def sol():
    n, k = map(int, input().split())
    cost = list(map(int, input().split()))
    nums = set(map(int, input().split()))

    graph = defaultdict(list)
    degree = [0] * (n)
    accumulate = [0] * (n)
    ans = [0] * (n)
    
    for i in range(n):
        line = list(map(int, input().split()))
        m, edges = line[0], line[1:]
        if i  + 1 in nums:
            continue
        degree[i] = m
        for a in edges:
            graph[a-1].append(i)

    queue = deque()
    for node in range( n ):
        if node +1 in nums:
            queue.append(node)
        elif degree[node] == 0:
            ans[node] = cost[node]
            queue.append(node)

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            degree[child] -= 1
            accumulate[child] += ans[node]
            if degree[child] == 0:
                queue.append(child)
                ans[child] = min(cost[child],accumulate[child])

    print(*ans)

T = int(input())
for _ in range(T):
	sol()