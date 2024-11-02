# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(2)]
class Solution:
    def __init__(self):
        self.root =TrieNode()
    def insert(self,num):
            cur  = self.root
            for i in range(32,-1,-1):
                bit = ((num>>i) & 1)
                if not cur.children[bit] :

                    cur.children[bit] = TrieNode()
            
                cur = cur.children[bit]

    def check(self,num):
            res = 0
            cur = self.root
            for  i in range(32,-1,-1):
                bit =((num >> i ) & 1)
                if cur.children[1-bit]:
                    res  |= (1<<i)
                    cur = cur.children[1-bit]  
                else:
                    cur = cur.children[bit]

            return res
            
        
    def findMaximumXOR(self, nums: List[int]) -> int:
       
            

        for num in nums:
            self.insert(num)

        ans = 0
        for num in nums:
            ans = max(ans,self.check(num))
        return ans
        






       
        
        
        
        
        
        
        

        
        
        
      








        
        
        
        
         

       



        



        





        