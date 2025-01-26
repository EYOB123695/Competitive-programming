# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0 
        val = capacity
        for i  in range(len(plants)):
            val -=  plants[i] 
            ans += 1 
            print(ans,val)
            if i != len(plants) -1 and  val < plants[i+1] : 
                ans += (i + 1) + (i +1 )
                val = capacity 
        return ans
            
            

        