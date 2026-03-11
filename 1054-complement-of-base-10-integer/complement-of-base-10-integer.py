class Solution:
    def bitwiseComplement(self, n: int) -> int:

        arr = [ ]
        if n == 0: 
            return 1
        while n > 0 : 
            val = n % 2 
           
            curr = "0" if val == 1 else "1"
            arr.append(curr) 
            n = n// 2
           
        c = 0 
        
        ans= 0 
        for i in range(len(arr)):
            ans += (int(arr[i]) * (2** c))
            c+=1
        return ans


