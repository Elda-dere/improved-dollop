class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        visted=set()
        graph=[[] for _ in range(n)]
        time=0
        for i in range(len(manager)):
            if -1 != manager[i]:
                graph[manager[i]].append(i)
            
        def dfs(node):
            visted.add(node)
            max_time=0
            for neighbour in graph[node]:
                if neighbour not in visted:
                    max_time=max(max_time,dfs(neighbour))
            return max_time+informTime[node]


        return (dfs(headID))