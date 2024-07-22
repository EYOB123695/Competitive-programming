# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for j in range(len(names)):
            for i in range(len(names)-1):
                if heights[i] < heights[i+1] :
                    heights[i+1] , heights[i] = heights[i] , heights[i+1]
                    names[i+1] , names[i] = names[i] , names[i+1]
                
           
        return names

