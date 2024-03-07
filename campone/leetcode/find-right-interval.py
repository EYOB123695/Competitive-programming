class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[b, e] for b, e in intervals]
        sorted_intervals = []
       

        for indx, [b, e] in enumerate(intervals):
            sorted_intervals.append([b, e, indx])

        sorted_intervals.sort(key=lambda x: x[0])
        begining_values = []

        for b, e, indx in sorted_intervals:
            begining_values.append(b)
        answer=[-1] *len(begining_values)    

        for b, e, indx in sorted_intervals:
            x=bisect.bisect_left(begining_values,e)
            if x!=len(begining_values):
                answer[indx]=sorted_intervals[x][-1]
            
        return answer

        