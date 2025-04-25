from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if state[node] != 0:
                return state[node] == 2  # already safe or found in cycle

            state[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False  # cycle detected
            state[node] = 2  # mark as safe
            return True

        result = []
        for i in range(n):
            if dfs(i):
                result.append(i)

        return result
