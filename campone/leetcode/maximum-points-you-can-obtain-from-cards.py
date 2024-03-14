class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        r = len(cardPoints) - k
        ans =  sum(cardPoints[r:])
        res = ans
        while r< len(cardPoints):
            ans += (cardPoints[l] - cardPoints[r])
            res = max(ans,res)
            l+=1
            r+=1
        return res
        