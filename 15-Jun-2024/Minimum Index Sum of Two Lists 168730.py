# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary = defaultdict(int)
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    dictionary[list1[i]] = i + j
        maxi = float(inf)
        for k,val in dictionary.items():
            maxi=  min(maxi,val)
        ans = []
        for k,v in dictionary.items():
            if v  == maxi:
                ans.append(k)
        return ans

        