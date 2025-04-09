# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        answer = 0 
        people.sort()
        l = 0 
        r = len(people) - 1
        while l <= r : 
            if people[l] + people[r] > limit :
                answer += 1 
                r-=1 
            elif people[l] + people[r] <= limit :
                 l += 1 
                 r -= 1 
                 answer += 1 
            

        return answer




        