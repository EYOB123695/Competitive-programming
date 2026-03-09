class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefixsum = [0] *len(s)
        prefixsum[-1] = shifts[-1]
        for i in range(len(s)-2,-1,-1):
            prefixsum[i] = shifts[i] + prefixsum[i+1]
        str = ""
        for i in range(len(prefixsum)):
            curr = ord(s[i])
            val = ( (( curr -97  ) + prefixsum[i]) % 26)
            str += chr(val+97) 
            
        return str



        