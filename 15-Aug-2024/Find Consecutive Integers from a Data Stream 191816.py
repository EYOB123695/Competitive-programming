# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        
        self.k = k 
        self.value = value 
        self.queue = deque()
        self.count = 0 
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count +=1 
       
        if len(self.queue) > self.k :
            if self.queue[0] == self.value:
                self.count -= 1 
            self.queue.popleft() 
      
        return self.k == self.count
         



        
        


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)