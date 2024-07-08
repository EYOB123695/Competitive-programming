# Problem: B - Your Hackathon Project - a Game - https://codeforces.com/gym/534160/problem/B

n,m = map(int,input().split())

arr = list(map(int,input().split()))
prefixsum = [0] *(n)
prefixsumtwo = [0] *(n)


for i in range(1,n):
    if arr[i-1] - arr[i] >0:
        d = arr[i-1] - arr[i]
    else:
        d = 0
    prefixsum[i] += prefixsum[i-1] + d
prefixsumtwo[-1] = 0
for j in range(n-2,-1,-1):
    
    if arr[j] - arr[j+1] < 0:
        d = abs(arr[j] - arr[j+1])
    else:
        d = 0
    prefixsumtwo[j] += prefixsumtwo[j+1] + d


for  i in range(m):
    arrtwo = [[]]
    s,t = map(int,input().split())
    if s < t: 
        print(prefixsum[t-1] - prefixsum[s-1])
    else:
        print(prefixsumtwo[t-1] - prefixsumtwo[s-1])


   
 

        

    
    