# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for i in s:
            
            res = []
            if i.isalpha():
                for j in ans:

                    res.append(j + i.lower())
                    res.append(j+i.upper())
            else:
                for j in ans:
                    res.append(j+i)
            ans = res 
        return ans 
            


                    

                     

            
            


        