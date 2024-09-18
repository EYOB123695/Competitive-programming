# Problem: C - Selecting Theatre Troupe - https://codeforces.com/gym/535749/problem/C



from math import comb

n, m, t = map(int,input().split())

res = 0
for b in range(4, t):
    res += comb(n, b)  * comb(m, t  - b)

print(res)