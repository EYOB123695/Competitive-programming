# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import sys
from collections import * 
sys.setrecursionlimit(10000)
def sol():
    n = int(input())
    arr = list(map(int,input().split()))
    s = input()
    graph  = defaultdict(list)
    ans = [0]
    for i in range(n-1):
        graph[arr[i] -1 ].append(i+1)
    
    def dfs(node):
        black , white  = 0 , 0 
        if s[node] == 'B':
            black +=1 
        else:
            white +=1 

        for nei in graph[node]:
            b, w = dfs(nei) 
            black += b 
            white += w 
      

        if black == white :
            ans[0] +=1 
        return black,white


    

    dfs(0)
    print(ans[0])

 
T= int(input())
for _ in range(T):
    sol()