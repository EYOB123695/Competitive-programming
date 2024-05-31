# Problem: A - Escaping Prison - https://codeforces.com/gym/513152/problem/A

def sol():
    n ,d = map(int,input().split())
    width =[ ]
    height = []
    for i in range(n):
        w,h = map(int,input().split())
        width.append(w)
        height.append(h)
    
    for i in range(len(width)):
        if width[i] > height[i]:
            d-=width[i]
        else:
            d-=height[i]
    
    if d <= 0:
        return "YES"
    else:
        return "NO"
    

        







T = int(input())
for _ in range(T):
    print(sol())