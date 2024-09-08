# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[[],[]]
        dict={}
        for i in matches:
            dict[i[1]] =  dict.get(i[1],0)+1
            dict[i[0]] =  dict.get(i[0],0)+0
        for key,val in dict.items():
            if val==0:
                ans[0].append(key)
            if val==1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans
        