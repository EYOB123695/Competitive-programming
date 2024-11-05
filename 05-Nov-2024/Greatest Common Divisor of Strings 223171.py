# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcd(a,b):
        while b:
            a, b = b ,a % b
        return a 

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        gcdlen = gcd(len(str1),len(str2))
        choice = str1[:gcdlen]
        if choice * (len(str1) // gcdlen) == str1 and choice * ((len(str2) // gcdlen)) == str2 :
            return choice 
        else:
            return ""


        

        
            
        






        