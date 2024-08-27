# Problem: G - Small Town - https://codeforces.com/gym/543431/problem/G

def sol():
    n= int(input())
    arr =list(map(int,input().split()))
    arr.sort()
    l = 0 
    r = max(arr)
    def check(mid):
        count = 1
        k = arr[0]
        for i in arr:
            if (i - k+1) // 2 > mid:
                k = i 
                count += 1 
        return count <= 3
    while l <= r:
        mid = (l+ r)// 2
        if check(mid):
            r = mid -1 
        else:
            l = mid +1  
    return l 

T = int(input())
for _ in range(T):
    print(sol())