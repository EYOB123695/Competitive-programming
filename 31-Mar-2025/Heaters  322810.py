# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        left = 0
       
        def checker(radius):
            j = 0
            for house in houses:
                while j < len(heaters) and heaters[j] < house - radius:
                    j += 1
                if j == len(heaters) or heaters[j] > house + radius:
                    return False
            return True 

        heaters.sort()
        houses.sort()
        right = max(houses[-1] - heaters[0] , heaters[-1] - houses[0])
        answer = 0
        while left <= right:
            mid = left + (right - left) //  2 
            if checker(mid):
                answer = mid 
                right = mid - 1 

            else:
                left = mid  + 1 
        return answer
            








    
        
         





            



        