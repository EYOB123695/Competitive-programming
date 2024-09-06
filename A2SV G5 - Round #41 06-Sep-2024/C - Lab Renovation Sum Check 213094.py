# Problem: C - Lab Renovation Sum Check - https://codeforces.com/gym/545013/problem/C

n = int(input())
matrix = []
for j in range(n):
    row = list(map(int,input().split()))
    matrix.append(row) 

ans = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 1:
            rows = []
            cols = []
            for k in range(n):
                if k != i:
                    rows.append(matrix[k][j])
            for z in range(n):
                if z != j:
                    cols.append(matrix[i][z]) 
            flag = False
            for p in range(len(cols)):
                for l in range(len(rows)):
                    if rows[l] + cols[p] == matrix[i][j]:
                        flag = True 
            if not flag :
                print("No")
                exit()
                      
print("Yes")
                        
                





            
