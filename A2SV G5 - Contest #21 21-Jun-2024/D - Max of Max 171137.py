# Problem: D - Max of Max - https://codeforces.com/gym/530187/problem/D

def sol():
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    def check(mid):
        for i in range(n):
            val = mid
            operations = 0
            

            for j in  range(i,n):
                if arr[j] < val and j == n-1:
                    operations = k+1
                    break
                if arr[j] >= val:
                    break
                operations +=  val  - arr[j]
                val = max(val-1,0)
            if operations <= k:
                return True
        return False
    l = max(arr)
    r = max(arr) + min(k,n)
    while l <= r:
        mid = l+(r-l) //2 
        if check(mid):
            l = mid+1 
        else:
            r = mid-1 
    return r


T = int(input())
for _ in range(T):
    print(sol())  
