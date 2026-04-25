class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        val = defaultdict(int)
        count = 0
        l = 0
        for i in range(len(s)):
            if s[i] in val :
                while s[i] in val :
                    val[s[l]] -= 1 
                    
                    if val[s[l]] == 0 :
                        del val[s[l]]
                    l += 1

                val[s[i]] += 1 
            else :
                val[s[i]] += 1
                count = max( (i - l +1) ,count )
                print(count,val)
        return count






        