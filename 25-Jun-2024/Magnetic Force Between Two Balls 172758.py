# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(mid):
            count = 1
            i = position[0]
            for j in range(1,len(position)):
                if i + mid <= position[j]:
                    count += 1  
                    i = position[j]
            if count >= m:
                return True 
            else:
                return False



        
        low = 1
        high = (max(position) - min(position)) + 1 
        while low <= high:
            mid  = low +(high - low) // 2 
            if check(mid):
                low = mid +1 
            else :
                high =  mid -1
        return high


        