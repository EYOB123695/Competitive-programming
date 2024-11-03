# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class Treenode():
    def __init__(self,start,end):
        self.left= None
        self.right = None
        self.start = start
        self.end = end
    def insert(self,start,end):
        cur = self
        while True:
            if start >= cur.end:
                if not cur.right:
                    cur.right = Treenode(start,end)
                    return True
                else:
                    cur = cur.right
            elif end <= cur.start:
                if not cur.left:
                    cur.left = Treenode(start,end)
                    return True
                else:
                    cur = cur.left
            else:
                return False





class MyCalendar:

    def __init__(self):
        self.root = None
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Treenode(startTime,endTime)
            return True
        else:
            return self.root.insert(startTime,endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)