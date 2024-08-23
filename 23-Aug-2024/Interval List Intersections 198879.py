# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l= 0 
        r = 0
        ans = []
        while l < len(firstList) and r < len(secondList):
            if firstList[l][0] <= secondList[r][1] and secondList[r][1] >= firstList[l][0]:
                x  = max(firstList[l][0],secondList[r][0])
                y = min (firstList[l][1],secondList[r][1])
                if x <= y :
                    ans.append([x,y])
       
            if firstList[l][1] < secondList[r][1]:
                l+=1
            else :
                r+=1
        return ans
            






        