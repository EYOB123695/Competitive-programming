# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int,input().split()) 
arr = list(map(int,input().split()))
arrtwo = list(map(int,input().split()))
l = 0 
r = 0 
ans = []
while l < len(arr) and r < len(arrtwo) :
    if arr[l] <= arrtwo[r] :
        ans.append(arr[l])
        l+=1 
    else :
        ans.append(arrtwo[r])
        r+=1 
while l != len(arr) :
    ans.append(arr[l])
    l+=1
while r != len(arrtwo) :
    ans.append(arrtwo[r])
    r+=1

res =" ".join(str(i) for i in ans) 
print(res)