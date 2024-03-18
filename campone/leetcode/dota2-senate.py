class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senate = list(senate)
        d, r = deque() , deque()
        for i, val in enumerate(senate):
            if  val == "R":
                r.append(i)
            else :
                d.append(i) 
        while d and r :
            left = d.popleft()
            right = r.popleft()
            if left < right :
                d.append(left + n ) 
            else:
                r.append(right + n) 
        if r :
            return "Radiant" 
        else :
           return  "Dire"




        