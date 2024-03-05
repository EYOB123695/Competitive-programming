class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myList = { 
        "2": ["a", "b", "c"], 
        "3": ["d", "e", "f"], 
        "4": ["g", "h", "i"], 
        "5": ["j", "k", "l"], 
        "6": ["m", "n", "o"], 
        "7": ["p", "q", "r", "s"], 
        "8": ["t", "u", "v"], 
        "9": ["w", "x", "y", "z"] }
        res=[]
        bucket=[]
        def backtrack(i):
            if len(bucket) == len(digits):
                res.append("".join(bucket.copy()))
                return 
            for j in myList[digits[i]]:
                bucket.append(j)
                backtrack(i+1)
                bucket.pop()


        if digits == "" :
            return []
        backtrack(0)
        return res
        

        