class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x : - abs(x[0]-x[1]) )
        B = A = len(costs) // 2 
        total = 0 
        for acost,bcost in costs:
            if B==0 or (A > 0 and acost <= bcost):
                total+=acost
                A-=1
            else:
                total+=bcost
                B-=1
        return total
        