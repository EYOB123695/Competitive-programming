# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
       
        arr = sorted(zip(difficulty,profit))
        currprofit = 0
        currdifficulity = 0 
        ability =  []
        profits = []
        for d,p in arr:
            if p > currprofit:
                currprofit = p
            ability.append(d)
            profits.append(currprofit)
        ans = 0
       
        for i in worker:
            l =  0
            h = len(ability) - 1 
            idx = float("inf")
            while l <= h:
                mid = l+ (h-l) // 2 
                if ability[mid] > i :
                    h = mid - 1 
                else: 
                    idx  = mid
                    l = mid  + 1 
            if idx != float("inf"):
                ans += profits[idx]
            
                     
        return ans
                

            


        

        


        