# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        rem =  0
        while numBottles >= numExchange:
            new =  numBottles // numExchange
            rem = numBottles % numExchange 
            numBottles = rem + new
            ans += new 
        return ans
        