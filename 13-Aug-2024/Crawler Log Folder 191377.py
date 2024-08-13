# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        paths_stack: list[str] = []

        for log in logs:
            if log == "../":
                if paths_stack:
                    paths_stack.pop()
            elif log != "./":
                paths_stack.append(log)

        return len(paths_stack)
        