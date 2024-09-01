# Problem: C - Permutation Sorting - https://codeforces.com/gym/538762/problem/C

T= int(input())
for _ in range(T):
    n= int(input())
    arr = list(map(int,input().split()))
    ans= 0 
    x = set()
    for i in arr:
        if i+1 in x:
            ans += 1
        x.add(i)
    print(ans)


