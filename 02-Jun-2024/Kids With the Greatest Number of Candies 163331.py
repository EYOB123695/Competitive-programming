# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [0] * (len(candies))
        print(res)
        val = max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= val:
                res[i]  = True 
            else:
                res[i] = False 
        return res
        