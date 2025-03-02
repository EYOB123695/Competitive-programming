# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:

        dict = Counter(word)
        val = []

        for k, v in dict.items():
            val.append(v)
        for i in range(len(val)):
            val[i] -= 1 
            if len(set(val)) == 1 :
                return True
            if val[i] == 0 :
                if len(set(val)) == 2:
                    return True
            val[i] += 1 
        return False


            
        




            





        