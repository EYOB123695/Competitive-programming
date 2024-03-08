class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans=[0] * k 
        unfairness= float ("inf")
        def backtrack(i):
            nonlocal unfairness, ans 
            if  i  == len(cookies):
                unfairness = min(unfairness,max(ans)) 
            if  unfairness <= max(ans):
                return
                return 
            for j in range(k) :
                ans[j] += cookies[i]
                backtrack(i+1)
                ans[j] -= cookies[i] 
        backtrack(0)
        return unfairness        





        