class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        dict=Counter(arr1)
        for a in arr2:
            
            for i in range(dict[a]):
                ans.append(a)  
        arr1.sort()
        
        for x in arr1:
            if x not in arr2:
                ans.append(x)
        return ans 