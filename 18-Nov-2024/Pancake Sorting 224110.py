# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips=[]
        n=len(arr)
        for i in range(n,1,-1):
            maxi=arr.index(i)
            if maxi != i-1:
                if maxi!=0:
                    arr=arr[:maxi+1][::-1] + arr[maxi+1:]
                    flips.append(maxi+1)
                arr = arr[:i][::-1] + arr[i:]
                flips.append(i)
        return flips
            

        
        

        