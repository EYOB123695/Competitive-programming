# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    c = 0

    for i in range(n):
        if s[i] != ")":
            c = 0
        else:
            c+=1
    
   
    if c > n - c:
        print("Yes")
    else:
        print("No") 
