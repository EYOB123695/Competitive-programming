class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max=0
        for i in range(len(points)-1):
            diff = points[i+1][0] - points[i][0]
            if diff > max:
                max= diff
        return max
            
        