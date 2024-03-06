class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l,h=0,len(citations) -1
        ans=0

        while l <= h:
            mid= l+(h-l)//2
            p=len(citations) - mid 
            
            if citations[mid] >= p :
                ans=p 
                h=mid-1
            else:
                l=mid+1
        return ans      