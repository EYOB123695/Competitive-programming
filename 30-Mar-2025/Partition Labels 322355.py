# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        dict= {}
        for i, c in enumerate(s):
            dict[c]=i
        res=[]
        size,end = 0 ,0

        for i, c  in enumerate(s):
            size+=1
            
            end = max(end,dict[c])
            if i == end :
                res.append(size)
                size=0
        return res

        