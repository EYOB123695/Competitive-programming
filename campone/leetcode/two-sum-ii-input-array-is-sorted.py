class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        ans=[]
        while i < j:
            if numbers[i] + numbers[j] == target:
                ans.append(i+1)
                ans.append(j+1)
                break
            if numbers[i] + numbers[j] < target:

                i +=1
            if numbers[i] + numbers[j] > target:
                j-=1
        return ans
        