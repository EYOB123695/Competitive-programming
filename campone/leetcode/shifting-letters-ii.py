class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = []
        ans = [0] * len(s)
        n = len(s) + 1
        prefixsum = [0] * n
        arr = [0] * len(s)
        for i in range(len(s)):
            arr[i] = ord(s[i]) - 97
        print(arr) 
        for i in range(len(shifts)):
            
                if  shifts[i][2] == 0 :
                    l = shifts[i][0]
                    r =shifts [i][1] 
                    prefixsum[l] -= 1
                    prefixsum[r+1] += 1 
                if shifts[i][2] == 1 :
                    l = shifts[i][0]
                    r =shifts [i][1] 
                    prefixsum[l] += 1
                    prefixsum[r+1]  -= 1 
        l = 0 
        r =  0 
        print(prefixsum)
        for  i in range(1,len(prefixsum)):  
            prefixsum[i] += prefixsum[i -1] 
        


        while l < len(arr) and r < len(prefixsum):
            prefixsum[l] += arr[r] 
            prefixsum[l] = prefixsum[l] % 26
            l+=1
            r+=1 
        print(prefixsum)
        for i in prefixsum:

            res.append( chr(i+97) )
        return "".join(res[:-1])
        


        


                    


                
        