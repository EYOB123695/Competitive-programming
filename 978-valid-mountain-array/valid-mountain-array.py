class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        bool = True 
        j = 0 
        if len(arr) < 3 : 
            return False 
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                j += 1 
            elif arr[i] > arr[i+1]:
                break
            else : 
                return False 
        if j == len(arr)-1 or  j == 0:
            return False 
        for  i in range(j,len(arr)-1):
            if arr[i+1] < arr[i]:
                j+=1 
            else:
                return False 

        return True 


            




        