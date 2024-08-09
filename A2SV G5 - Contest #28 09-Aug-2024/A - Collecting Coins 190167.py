# Problem: A - Collecting Coins - https://codeforces.com/gym/540354/problem/A

T = int(input())
for _ in range(T):
    a,b,c,p = map(int,input().split())
    val = max(a,b,c)
    if a != val :
       
        p-= (val - a )
        a += (val -a )
    if b != val : 
        
        p-= (val - b )
        b += (val -b )
    if c != val:
        
        p-= (val - c )
        c += (val -c )
        
    if p < 0 or p % 3 != 0:
        print("NO")
    else:
        print("YES")
    
