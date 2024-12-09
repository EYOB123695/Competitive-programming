# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if (len(changed) % 2) != 0 :
            return []
        changed.sort()
        frequency = Counter(changed)
        answer = []
        for num in changed:
            if frequency[num] == 0:
                continue 
            if frequency[num * 2] == 0 : 
                print(frequency)
                return []
            answer.append(num)
            frequency[num] -= 1 
            frequency[num * 2 ] -= 1 
        return answer
            


       
        


        