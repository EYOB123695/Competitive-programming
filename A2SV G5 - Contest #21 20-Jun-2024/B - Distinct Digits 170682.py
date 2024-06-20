# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

def sol():
    n = int(input())
    res= ""
    for i in range(9,0,-1):
        if i <= n:
            res+=str(i)
            n-=i 
    
    res = res[::-1] 
    return int(res) 


            


T= int(input())
for _ in range(T):
    print(sol())
