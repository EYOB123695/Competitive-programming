# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

n = int(input())
l = 1 
r = n 
def check(mid,n):
    
    count = 0
    
    curr = n
    while curr > 0:
        mid = min(curr,mid)
        curr -= mid
        count += mid
        curr -= curr // 10
       


    return count * 2 >= n
ans =  n
while l<= r :
    mid = l + (r-l)//2 
    if check(mid,n):
        ans = mid
        r = mid -1 
    else:
        l = mid +1 
print(ans)
    