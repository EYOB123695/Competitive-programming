# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

def sol():
    n = int(input())
    matrix = []
    
    for j in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
    arr = [2**30 -1 ] * n
    
    for i in range(n):
        for j in range(n):
            if i != j:
                arr[i] &= matrix[i][j]
                arr[j] &= matrix[i][j]
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] | arr[j] != matrix[i][j]:
                print ("NO")
                return
            
            
    print("YES")
    print(*arr)

T = int(input())
for  _ in range(T):
    sol()
  