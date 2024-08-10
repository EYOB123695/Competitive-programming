# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

T= int(input())
for _ in range(T):
    n,k = map(int,input().split())
    checkone  = False
    checktwo = False
    for i in range(n):
        
        l,r = map(int,input().split())
        if l == k:
            checkone = True 
        if r == k :
            checktwo =True 
    if checktwo and checkone:
        print("YES")
    else:
        print("NO")
