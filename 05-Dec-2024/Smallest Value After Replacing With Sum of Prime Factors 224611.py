# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int: 
        def factorize(n):
            i  = 2 
            factors = [ ]
            while i * i <= n :
                while n % i == 0:
                    factors.append(i) 
                    n //= i 
                i += 1
            if n > 1 :
                factors.append(n) 
            return factors  
       
        
        total = n
        seen = set()
        while total > 0 :
            arr = factorize(total) 
            if len(arr) == 1 :
                return sum(arr)
            total = sum(arr)
            if total in seen :
                break 
            seen.add(total)
        return total

        
        