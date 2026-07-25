class Solution:
    def maxProduct(self, n: int) -> int:
        array =[int(val) for val in str(n)]
        array.sort()
        return (array[-1] * array[-2])


        