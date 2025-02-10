# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

T = int(input())
for _ in range(T): 
    n,m = map(int , input().split())
    matrix = [ ]
    for i in range(n):
        row = list(map(int , input().split()))
        matrix.append(row)
    ans = -float("inf")
    def inbound(i,j):
        return 0<= i < n and 0<= j < m  
    
    
    for i in range(n): 
        for j in range(m):
            res= matrix[i][j]
            nr ,nc =   i + 1 ,j + 1 
            while inbound(nr,nc):
                res += matrix[nr][nc]
                nr += 1 
                nc += 1 
            nr ,nc =  i - 1 ,j - 1
            while inbound(nr,nc):
                res += matrix[nr][nc]

                nr-= 1 
                nc -= 1  
            nr ,nc =  i + 1 ,j - 1 
            while inbound(nr,nc):
                res += matrix[nr][nc]
                nr += 1 
                nc -= 1 
            nr ,nc =  i - 1 ,j + 1 
            while inbound(nr,nc):
                res += matrix[nr][nc]
                nr -= 1 
                nc += 1 
        
            ans = max(ans , res)
    print(ans) 


            




