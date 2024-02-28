class Solution:
    def sortSentence(self, s: str) -> str:
        arr=[""] * len(s)
        dict={}
        x = s.split()
        for c in x :
            dict[c[-1]] = c[:-1]
        
        
        for key,value in dict.items():
            z=int(key)
            arr[z] = value + " " 

                
                
        return "".join(arr).rstrip() 

        
            
        




        