# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans =  0 
        dict = Counter(answers)
        for k,v in dict.items():
            size =  k + 1
            group = (v + k) // size
            ans += group * size
        return ans




       







        