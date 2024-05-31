# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/513152/problem/B

import math
def sol():
    n,k = input().split()
    n= int(n)
    k = int(k) 
    d = list(map(int,input().split()))
    a = list(map(int,input().split()))
    
    def check(mid):
        hour = 0
        for i in range(len(d)):
           c = d[i] / mid
           add = math.ceil(c) 
           
           hour +=  add *  a[i]   
            
        if hour <= k :
            return True 
        else :
            return False 
             
    
    h = max(d)
    
    l = 1
    while l <= h : 
        mid = l+ (h-l) // 2
        if check(mid):
            h = mid-1
        else:
            l = mid+1 
    if l > max(d):
        return -1
    else:
        return l

        
    

         

    
        
T= int(input())
for _ in range(T):
    s=sol()
    print(s)
