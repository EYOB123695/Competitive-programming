# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixsum  = [0] *(n+1) 
        for l,r,val in  bookings:
            prefixsum[l-1] += val
            prefixsum[r] -= val 
        for i in range(1,len(prefixsum)):
            prefixsum[i] += prefixsum[i-1] 
        return prefixsum[:-1]



