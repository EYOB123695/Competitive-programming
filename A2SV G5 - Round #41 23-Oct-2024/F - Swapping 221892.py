# Problem: F - Swapping - https://codeforces.com/gym/544853/problem/D

t = int(input())
for _ in range(t):
    n, k, m = list(map(int, input().split()))
    start = k
    end = k
    
    for i in range(m):
        l, r = map(int, input().split()) 
        if l <= start <= r or l <= end <= r:
            start = min(start, l)
            end = max(end, r)
    print(end - start + 1)
