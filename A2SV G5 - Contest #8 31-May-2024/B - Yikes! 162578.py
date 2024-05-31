# Problem: B - Yikes! - https://codeforces.com/gym/511242/problem/B

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))
prefixsum = [0] * (len(arr)+1)


for i in range(1,len(prefixsum)):
    prefixsum[i] = prefixsum[i-1] + arr[i-1]


for i in query:
    l = 0
    r = n
    while l <= r:
        mid  = l+(r-l) // 2 
        if prefixsum[mid] < i:
            l = mid+1
        else:
            r  =mid -1
    print(l)


