# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        l = 0 
        ans = 0
        total = 0 

        for r in range(len(fruits)):
            count[fruits[r]]+= 1
            total +=1 
            while len(count) > 2 :
                f = fruits[l]
                count[f] -= 1
                total -= 1 
                l+=1
                if not count[f]:
                    del count[f] 
            ans = max(ans,total)
        return ans