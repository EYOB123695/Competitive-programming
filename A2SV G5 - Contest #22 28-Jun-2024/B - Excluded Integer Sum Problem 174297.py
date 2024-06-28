# Problem: B - Excluded Integer Sum Problem - https://codeforces.com/gym/531455/problem/B

T = int(input())
for _ in range(T):

    n,k,x = map(int,input().split())
    arr= []
    if x != 1:
        print("YES")
        print(n)
        print(*([1]*n))
    elif k == 1 :
        print("NO")
    elif k == 2 and (n % 2 != 0):
        print("NO")
      
    else:
        print("YES")
        print(n//2)
        for i in range((n//2)-1):
            arr.append(2) 
        if n % 2 == 0:
            arr.append(2)
        else:
            arr.append(3)
        print(*arr)
        


    
          


