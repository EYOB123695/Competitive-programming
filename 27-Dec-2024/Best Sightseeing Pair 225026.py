# Problem: Best Sightseeing Pair - https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = -float("inf")
        current_value = values[0] - 1  
        for i in range(1 , len(values)):
            answer = max(values[i] + current_value , answer)
            current_value= max(current_value-1  , values[i] -1) 
            print(answer,current_value)
        return answer


