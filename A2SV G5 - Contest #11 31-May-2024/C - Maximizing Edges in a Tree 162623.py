# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u,v = map(int,input().split())

    graph[u].append(v)
    graph[v].append(u)

color = [-1] * (n+1)
stack = [1]
color[1] = 0
countone = 0
counttwo = 0
while stack:
    val = stack.pop()
    if color[val] == 0:
        countone+=1
    else:
        counttwo+=1
    child = 1 - color[val]
    for adj in graph[val]:
        if color[adj] == -1: 
            color[adj] = child
            stack.append(adj)

        


final = countone * counttwo
print(final - (n-1))