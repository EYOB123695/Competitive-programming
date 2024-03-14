class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixsum = [0] * (n + 1) 
        for l,r,add in bookings:
            prefixsum[l-1]+=add
            prefixsum[r] -= add
        for i in range(1,len(prefixsum)):
            prefixsum[i] += prefixsum[i-1]
        return prefixsum[:-1]
            
