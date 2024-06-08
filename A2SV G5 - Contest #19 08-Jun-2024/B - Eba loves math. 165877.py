# Problem: B - Eba loves math. - https://codeforces.com/gym/527294/problem/B

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    val = min(arr)
    for i in arr:
        val  = val & i
    print(val)
    
    
    
    
       
       
    
    

    

    