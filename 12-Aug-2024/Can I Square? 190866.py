# Problem: Can I Square? - https://codeforces.com/contest/1915/problem/C

T = int(input())
for i in range(T):
    n= int(input())
    arr = list(map(int,input().split()))
    x = sum(arr)
    y = x ** 0.5 
  
    if y.is_integer():
        print("YES")
    else:
        print("NO")