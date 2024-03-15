class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        li = list(s) 
        count = 0 
        ans = 0 
        l = 0 
        r = len(s) -1

        while l <  r :
            if li[l] == "1" and li[r] == "0":
                li[l],li[r] = li[r],li[l]
                count+=(r-l)
                l+=1
                r-=1
            elif li[l] == "0" and li[r] == "0":
                l+=1
                
            elif li[l] == "1" and li[r] == "1" : 
                r-=1
            else:
                l+=1
                r-=1
        return count


            