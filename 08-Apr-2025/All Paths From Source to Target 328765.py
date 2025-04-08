# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        build_graph = defaultdict(list)
        for idx,val in enumerate(graph):
            build_graph[idx].append(val)
        res = []
        def dfs(currnode,currlist):
            if currnode == len(graph) -1 :
                res.append(list(currlist))
            for nei in graph[currnode]:
                currlist.append(nei)
                dfs(nei,currlist)
                currlist.pop()
        dfs(0,[0])
        return res


        