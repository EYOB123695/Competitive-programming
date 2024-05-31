# Problem: B - Mapping the Maze - https://codeforces.com/gym/515998/problem/B

from collections import defaultdict 
def sol(edges):
    graph = defaultdict(list) 
    for i in edges:
        graph[i[0]].append(i[1])
 
 
 
    return graph
 
 
 
 
 
 
 
 
 
 
 
 
 
 
n, m = map(int, input().split())
flag = False
edges= []
for _ in range(m): 
    x, y = map(int, input().split())
    edges.append([x,y]) 
graph=sol(edges)
 
ans= defaultdict(int)
for key,val in graph.items():
    x = len(val)
 
    ans[key] += x
    for i in val :
        ans[i] += 1 
 
#print(ans) 
#print(graph)
count = 0
counttwo = 0 
for key,val in ans.items():
    if val == n-1 :
        
        flag = True
 
    
    elif val == 1 :
        count += 1
    elif val == 2 :
        counttwo+=1
 
if count == 2  and counttwo == n-2  :   
    print("bus topology") 
elif flag and count == n-1:
    print("star topology") 
elif counttwo == n:
    print("ring topology") 
else :
    print("unknown topology")