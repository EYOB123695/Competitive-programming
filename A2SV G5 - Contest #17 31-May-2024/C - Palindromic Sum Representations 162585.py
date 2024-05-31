# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

dp  =[1] +  [0] * (40001)
def sol(n):
    mod = 10 ** 9 + 7
    

    for i in range(1 , n + 1):
        x = str(i)
        if x == x[::-1]:
            for j in range(i, n + 1):
                
                dp[j] = (dp[j]  +  dp[j - i])% mod

arr = []
T= int(input())
for _ in range(T):
    x = int(input())
    arr.append(x)
val = max(arr)
sol(val+ 1)
for i in arr:
    print(dp[i])