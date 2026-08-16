class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        # Count frequencies of stone values modulo 3
        count = [0, 0, 0]
        for s in stones:
            count[s % 3] += 1
        
        c0, c1, c2 = count[0], count[1], count[2]
        
        # If the count of 0-remainder stones is even:
        # Alice wins if both remainder 1 and remainder 2 stones exist.
        if c0 % 2 == 0:
            return c1 >= 1 and c2 >= 1
        
        # If the count of 0-remainder stones is odd:
        # The parity flip gives Bob an advantage unless the difference
        # between remainder 1 and remainder 2 stones is strictly greater than 2.
        return abs(c1 - c2) > 2