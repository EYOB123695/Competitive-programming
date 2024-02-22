class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)

              
        i=0
        h=len(s)-1
        while i < h:

            s[i] , s[h] = s[h] ,s[i]
            i = i +1
            h = h-1

        