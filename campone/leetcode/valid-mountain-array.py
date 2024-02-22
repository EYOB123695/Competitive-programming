class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # n=len(arr)
        # max=0
        # i=0
        # j=i+1
        # for j in range(n) :
        #     if arr[j] > arr[i]:
        #         continue
        #     if arr[j] < arr[i]:
        #         max = arr[i]
                
                
        #     if max != 0 and arr[j] >= max :
        #         return False

        #     i+=1  
        # return True

        # from start to middle
        if len(arr) < 3:
            return False

        idx = 1
        inc = False
        while idx < len(arr) and arr[idx] > arr[idx-1]:
            inc = True
            idx += 1
        
        if not inc:
            return False

        dec = False
        while idx < len(arr) and arr[idx] < arr[idx-1]:
            dec=True
            idx+=1
        if dec and idx == len(arr):
            return True
        return False
        


        



        # from middle to end
        