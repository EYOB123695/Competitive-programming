# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue=  deque()
        queue.append([1,0])
        visited  = set()
        board = board[::-1]
        def convert(i):
            r = (i-1) // n
            c = (i-1) % n
            if r % 2 != 0:
                c = n - 1 - c
            return [r,c]


        while queue:
            val,ans  = queue.popleft()
            for i in range(1,7):
                nextval = val +i 
                r,c  = convert(nextval)
                if board[r][c] != -1:
                    nextval = board[r][c] 
                if nextval == n * n:
                    return ans +1 
                if nextval not in visited:
                    visited.add(nextval)
                    queue.append([nextval,ans+1])
                    
        return -1



        
        