from collections import defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]):

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        infected = set()

        def dfs(node):
            if node in infected:
                return
            infected.add(node)
            for nxt in graph[node]:
                dfs(nxt)

        dfs(k)

        for u, v in invocations:
            if u not in infected and v in infected:
                return list(range(n))

        return [i for i in range(n) if i not in infected]