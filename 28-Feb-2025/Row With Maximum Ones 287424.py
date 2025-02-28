# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = -float("inf")
        result = []
        for i in range(len(mat)) :
            answer = 0 
            for j in range(len(mat[0])):
                if mat[i][j] == 1 :
                    answer  += 1
            if answer > count:
                result.append(i)
                result.append(answer)
                count = answer
        return result[-2:] 


            





        