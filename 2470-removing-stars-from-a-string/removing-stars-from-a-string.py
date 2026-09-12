class Solution:
    def removeStars(self, s: str) -> str:
        skip = 0 
        ans = []
        for i in reversed(s):
            if i ==  "*" :
                skip += 1
            elif skip :
                skip -= 1
            else : 
                ans.append(i)
        return ("").join(reversed(ans))





        