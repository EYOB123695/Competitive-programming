class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dictone=defaultdict(int)
        dict=defaultdict(int)
        for i in nums1:
            dict[i] +=1 
        for j in nums2:
            dictone[j] +=1

        for i in nums2:
            if dict[i] > 0:
                ans.append(i)
                dict[i]-=1
        return ans

            

        