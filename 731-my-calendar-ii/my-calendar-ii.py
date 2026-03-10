class MyCalendarTwo:

    def __init__(self):
        self.nonoverlapping = []
        self.overlapping = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s,e in self.overlapping:
            if not (e <= startTime or s >= endTime):
                return False
        for s,e in self.nonoverlapping:
            if not (e <= startTime or s >= endTime):
                self.overlapping.append((max(s,startTime),min(e,endTime)))
        self.nonoverlapping.append((startTime,endTime))
        return True


     


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)