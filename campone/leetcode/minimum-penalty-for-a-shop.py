class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        prefix = [0] * (n+1)
        postfix = [0] * (n+1) 

        for i in range(1,n+1):
            prefix[i] = prefix[i-1] 
            if customers[i-1] == "N":
                prefix[i] +=1 
        for i in range(n-1,-1,-1):
            postfix[i] = postfix[i+1]
            if  customers[i] == "Y":
                postfix[i] += 1 
        min = float("inf")
        idx  = 0 
        for i in range(n+1):
            sum = prefix[i] + postfix[i]
            if sum < min :
                min = sum 
                idx  = i

        return idx
