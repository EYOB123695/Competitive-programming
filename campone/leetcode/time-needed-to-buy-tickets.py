class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        for i in range(len(tickets)):
            if tickets[i] - tickets[k] >=0 and k>=i:
                time+=tickets[k]
            elif tickets[i]-tickets[k] >=0 and k<i:
                time+=tickets[k]-1
            elif tickets[i] -tickets[k] <0: 
                time+=tickets[i]
        return time