# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arrtwo = list(map(int,input().split()))
n = len(arr)
m = len(arrtwo)
l = 0 
r = 0 
ans = []
while l < n and r < m: 
    if arr[l] <= arrtwo[r]:
        ans.append(arr[l])
        l += 1 
    else:
        ans.append(arrtwo[r])
        r += 1 
while l < n :
    ans.append(arr[l])
    l+= 1 
while r < m:
    ans.append(arrtwo[r])
    r += 1 
print(" ".join(map(str,ans)))
