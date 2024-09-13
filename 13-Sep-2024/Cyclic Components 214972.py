# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E


from collections import *
n,m = map(int,input().split())
graph = defaultdict(list)
degree=[0 ] * (n+1)
for _ in range(m):
    l,r = map(int,input().split())
    graph[l].append(r)
    graph[r].append(l)
    degree[l] +=1 
    degree[r]+=1 
    
count = 0 
visited = [False] *(n +1)

def dfs(i):
    comp = [ ]
    stack = [i]
    visit = set()
   
    while stack:
        val = stack.pop()
        
        if not visited[val]:
            visited[val] = True
            comp.append(val)
        for nei in graph[val]:
            if not visited[nei]:
                stack.append(nei)
                
    return all(degree[node] == 2 for node in comp)
                

          
    
        
    


for i in range(1,n+1):
    if not visited[i]:
        if dfs(i):
            count += 1
       
            
        
print(count)

