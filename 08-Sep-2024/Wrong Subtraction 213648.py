# Problem: Wrong Subtraction - https://codeforces.com/problemset/problem/977/A?mobile=false

n,k = map(int , input().split())
while k:
    if n % 10 == 0 :
        n //= 10 
    else:
        n -=1  
    k-= 1 
print(n)