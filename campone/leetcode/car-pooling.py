class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
     
       # 4 
        #0  0  0  0  0  0   0   0 
        #0  2  0  0  0   0  -2 0
        #0  0  0  3 0   0   -3  0   
        #0  2  0  3 3   0  -2   0
        #0   2 2   5  2  2   0  0 
        
        trips.sort(key = lambda t: t[2])
        for  i in range(len(trips)):
            n = trips[i][2]
        #print(n)
      
        prefixsum =  [0] * (n + 1)   
    
        for  i in range(len(trips)):
            c = trips[i][0]
            l = trips[i][1]
            r = trips[i][2]
           
            prefixsum[l] += c 
            prefixsum[r] -= c  
        
        for i in range(1,len(prefixsum)):
            prefixsum[i] += prefixsum[i-1] 
        print(prefixsum)
        for i in prefixsum:
            if  capacity < i :
                return False 
            
        return True
        
         




