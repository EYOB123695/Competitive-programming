# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dictionary = defaultdict(int)
        for i in arr:
            dictionary[i%k] += 1 
        for key,freq in dictionary.items():
            if key !=0 and freq != dictionary[k - key]:
                print (key)
                return False 
        if (dictionary[0] % 2 )!= 0 :
            print(dictionary[0])
            return False 
        return True


        


