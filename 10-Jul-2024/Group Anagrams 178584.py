# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic  = defaultdict(list)
        for s in strs:
            res = [0] * 26
            for i in s:
                res[ord(i) - ord("a")] +=1
            dic[tuple(res)].append(s)
        final = []
        for k,v in dic.items():
            final.append(v)
        return final 

        
        