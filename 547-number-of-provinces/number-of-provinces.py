class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        root = [i for i in range(len(isConnected)) ]
        size = [1] * len(isConnected)
        ans = len(isConnected)
        def find(x):
            if  x == root[x]:
             return x 
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            parentx = find(x)
            parenty = find(y)
            if parentx != parenty:
               
                if size[parentx] > size[parenty]:
                    root[parenty] = parentx
                    size[parentx] += size[parenty]
                else:
                    root[parentx] = parenty
                    size[parenty] += size[parentx] 
                return True 
            return False
        
        
        for i  in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 :
                    if  union(i,j):
                      ans-=1
        return ans




        