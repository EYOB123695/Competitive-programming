# Problem: D -  Longest Good Sequence - https://codeforces.com/gym/524965/problem/D


 
n = int(input())
 
nums = list(map(int, input().split()))
if n == 1 and nums[0] == 1:
    print(1)
    exit()
 
def find_divisors(number):
    divisors = []
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
 
    return divisors  
 
 
dp = [0] *(max(nums) + 1)
 
for num in nums:
    divisors = find_divisors(num)
    dp[num] = 1
    for div in divisors:
        dp[num] = max(dp[num], dp[div] + 1)
 
    for div in divisors:
        dp[div] = max(dp[div], dp[num])
print(max(dp))